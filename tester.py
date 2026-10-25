#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Github-Gemini Subscription Builder
Cross-platform (Linux/GitHub Actions + Windows local) proxy tester:
download subs -> dedup -> parallel xray test (latency + country + deep Gemini check)
-> rename with flags -> write base64 subscription.

Stdlib only. Works with any Xray-core binary passed via --xray (or found in
standard locations on Windows).
"""

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------------------------------------------------------------- constants

SCHEMES = ("vless://", "vmess://", "trojan://")
CURL = "curl.exe" if os.name == "nt" else "curl"
FLAG_GEMINI = "\u264a"                      # ♊
FLAG_BELIZE = "\U0001f1e7\U0001f1ff"        # 🇧🇿 — makes US sort to top in clients
FLAG_WORLD = "\U0001f310"                   # 🌐
BLOCKED_PATTERNS = (
    "not supported in your country",
    "isn't supported in your country",
    "not currently available in your country",
)
MIN_GEMINI_HTML_LEN = 2500
XRAY_CANDIDATES_WIN = [
    r"C:\Program Files\FlyFrogLLC\Happ\core\xray.exe",
    r"C:\v2rayN\bin\Xray\xray.exe",
    r"C:\v2rayN\xray\xray.exe",
]

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_print_lock = threading.Lock()


def tprint(msg):
    with _print_lock:
        print(msg, flush=True)


# ---------------------------------------------------------------- helpers

def b64_decode(s):
    s = s.strip().rstrip("=")
    s += "=" * ((4 - len(s) % 4) % 4)
    return base64.b64decode(s).decode("utf-8", "ignore")


def flag_of(loc):
    u = (loc or "").upper()
    if len(u) == 2 and u.isalpha() and u.isascii():
        return chr(0x1F1E6 + ord(u[0]) - 65) + chr(0x1F1E6 + ord(u[1]) - 65)
    return FLAG_WORLD


def split_host_port(s):
    """host:port with IPv6 ([::1]:443) support."""
    s = s.strip()
    if s.startswith("["):
        host, _, rest = s[1:].partition("]")
        return host, int(rest.lstrip(":"))
    host, _, port = s.rpartition(":")
    return host, int(port)


def parse_params(query):
    return {k.lower(): urllib.parse.unquote(v) for k, _, v in
            (kv.partition("=") for kv in query.split("&")) if k}


def find_xray(explicit):
    if explicit:
        if os.path.isfile(explicit):
            return explicit
        return None
    for p in XRAY_CANDIDATES_WIN:
        if os.path.isfile(p):
            return p
    for p in ("./bin/xray", "./bin/xray.exe", "./xray", "./xray.exe"):
        if os.path.isfile(p):
            return os.path.abspath(p)
    path = os.environ.get("PATH", "")
    for d in path.split(os.pathsep):
        c = os.path.join(d, "xray.exe" if os.name == "nt" else "xray")
        if os.path.isfile(c):
            return c
    return None


# ---------------------------------------------------------------- link -> xray outbound

def parse_vless(link):
    raw = link[8:]
    if "#" in raw:
        raw = raw.split("#", 1)[0]
    if "@" not in raw:
        return None
    uuid_part, rest = raw.rsplit("@", 1)
    hp, _, query = rest.partition("?")
    addr, port = split_host_port(hp)
    p = parse_params(query)
    net = p.get("type", "tcp")
    if net in ("h2", "http"):
        net = "http"
    sec = p.get("security", "none")
    sni = p.get("sni") or addr
    fp = p.get("fp", "chrome")
    path = p.get("path", "/")
    pbk, sid = p.get("pbk", ""), p.get("sid", "")

    user = {"id": uuid_part, "encryption": "none"}
    if p.get("flow"):
        user["flow"] = p["flow"]

    outbound = {
        "tag": "proxy",
        "protocol": "vless",
        "settings": {"vnext": [{"address": addr, "port": port, "users": [user]}]},
        "streamSettings": {"network": net, "security": sec},
    }
    ss = outbound["streamSettings"]
    if sec == "reality":
        ss["realitySettings"] = {"show": False, "fingerprint": fp,
                                 "serverName": sni, "publicKey": pbk,
                                 "shortId": sid or ""}
    elif sec == "tls":
        ss["tlsSettings"] = {"serverName": sni, "fingerprint": fp,
                             "allowInsecure": True}
    if net == "ws":
        ws = {"path": path, "headers": {}}
        if p.get("host"):
            ws["headers"]["Host"] = p["host"]
        ss["wsSettings"] = ws
    elif net == "grpc":
        ss["grpcSettings"] = {"serviceName": p.get("servicename", path).lstrip("/"),
                              "multiMode": False}
    elif net == "httpupgrade":
        hu = {"path": path}
        if p.get("host"):
            hu["host"] = p["host"]
        ss["httpupgradeSettings"] = hu
    elif net == "http":
        hs = {"path": path}
        if p.get("host"):
            hs["host"] = [p["host"]]
        ss["httpSettings"] = hs
    return outbound


def parse_vmess(link):
    try:
        obj = json.loads(b64_decode(link[8:]))
    except Exception:
        return None
    addr = obj.get("add", "")
    if not addr:
        return None
    port = int(obj.get("port", 443))
    net = obj.get("net") or "tcp"
    if net in ("h2", "http"):
        net = "http"
    sec = obj.get("tls") or "none"

    outbound = {
        "tag": "proxy",
        "protocol": "vmess",
        "settings": {"vnext": [{"address": addr, "port": port, "users": [{
            "id": obj.get("id", ""), "alterId": int(obj.get("aid") or 0),
            "security": "auto"}]}]},
        "streamSettings": {"network": net, "security": sec},
    }
    ss = outbound["streamSettings"]
    if sec == "tls":
        ss["tlsSettings"] = {"serverName": obj.get("sni") or obj.get("host") or addr,
                             "allowInsecure": True}
    if net == "ws":
        ws = {"path": obj.get("path") or "/", "headers": {}}
        if obj.get("host"):
            ws["headers"]["Host"] = obj["host"]
        ss["wsSettings"] = ws
    elif net == "grpc":
        ss["grpcSettings"] = {"serviceName": (obj.get("path") or "").lstrip("/"),
                              "multiMode": False}
    elif net == "http":
        hs = {"path": obj.get("path") or "/"}
        if obj.get("host"):
            hs["host"] = [obj["host"]]
        ss["httpSettings"] = hs
    return outbound


def parse_trojan(link):
    raw = link[9:]
    if "#" in raw:
        raw = raw.split("#", 1)[0]
    password, rest = raw.rsplit("@", 1)
    hp, _, query = rest.partition("?")
    addr, port = split_host_port(hp)
    p = parse_params(query)
    sni = p.get("sni") or addr
    net = p.get("type", "tcp")
    if net in ("h2", "http"):
        net = "http"

    outbound = {
        "tag": "proxy",
        "protocol": "trojan",
        "settings": {"servers": [{"address": addr, "port": port,
                                  "password": urllib.parse.unquote(password)}]},
        "streamSettings": {"network": net, "security": "tls",
                           "tlsSettings": {"serverName": sni,
                                           "allowInsecure": True}},
    }
    if net == "ws":
        ws = {"path": p.get("path", "/"), "headers": {}}
        if p.get("host"):
            ws["headers"]["Host"] = p["host"]
        outbound["streamSettings"]["wsSettings"] = ws
    elif net == "http":
        hs = {"path": p.get("path", "/")}
        if p.get("host"):
            hs["host"] = [p["host"]]
        outbound["streamSettings"]["httpSettings"] = hs
    return outbound


PARSERS = {"vless://": parse_vless, "vmess://": parse_vmess,
           "trojan://": parse_trojan}


def link_outbound(link):
    for scheme, fn in PARSERS.items():
        if link.startswith(scheme):
            try:
                return fn(link)
            except Exception:
                return None
    return None


# ---------------------------------------------------------------- remark / renaming

def link_remark(link, fallback):
    if "#" in link:
        frag = link.split("#", 1)[1]
        if frag.strip():
            return urllib.parse.unquote(frag).strip()
    if link.startswith("vmess://"):
        try:
            return (json.loads(b64_decode(link[8:])).get("ps") or "").strip()
        except Exception:
            pass
    return fallback


def strip_old_prefix(name):
    # remove previously-added "XX flag ♊Gemini-" style prefixes
    return re.sub(r"^[A-Z]{2}\S{0,6}-\s*", "", name).strip() or "node"


def build_prefix(loc, gemini_ok):
    f = flag_of(loc)
    if gemini_ok:
        if loc.upper() == "US":
            return f"{FLAG_BELIZE}US{f}{FLAG_GEMINI}Gemini-"
        return f"{loc.upper()}{f}{FLAG_GEMINI}Gemini-"
    return f"{loc.upper()}{f}-"


def rename_link(raw, new_name):
    if raw.startswith("vmess://"):
        try:
            obj = json.loads(b64_decode(raw[8:]))
            obj["ps"] = new_name
            payload = json.dumps(obj, separators=(",", ":"), ensure_ascii=False)
            return "vmess://" + base64.b64encode(payload.encode("utf-8")).decode()
        except Exception:
            return raw
    clean = raw.split("#", 1)[0]
    return f"{clean}#{urllib.parse.quote(new_name, safe='')}"


def dedup_signature(link):
    """Same node seen in different subs -> same signature (fragment stripped)."""
    body = link.split("#", 1)[0].strip()
    if link.startswith("vmess://"):
        try:
            o = json.loads(b64_decode(body[8:]))
            if o.get("add") and o.get("port") and o.get("id"):
                return f"vmess://{o['add']}:{o['port']}:{o['id']}"
        except Exception:
            pass
    return body


# ---------------------------------------------------------------- subscription download

def fetch_url(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "v2rayN/6.23"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "ignore")


def content_to_links(content):
    if not re.search(r"(vless|vmess|trojan)://", content):
        try:
            dec = b64_decode("".join(content.split()))
            if re.search(r"(vless|vmess|trojan)://", dec):
                content = dec
        except Exception:
            pass
    return [l.strip() for l in re.split(r"\r?\n", content)
            if l.strip().startswith(SCHEMES)]


def download_subs(urls):
    """Returns (items[{raw, sub}], stats[{url, fetched, unique, ping, gemini}])."""
    from concurrent.futures import ThreadPoolExecutor

    def grab(url):
        last_err = None
        for attempt in (1, 2):
            try:
                return url, fetch_url(url), None
            except Exception as e:
                last_err = e
                time.sleep(1)
        return url, None, last_err

    contents = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futs = [pool.submit(grab, u) for u in urls]
        for fut in as_completed(futs):
            url, text, err = fut.result()
            if err is None:
                contents[url] = text
            else:
                tprint(f"    [!] download failed: {url} ({err})")

    seen, items, order = {}, [], []
    for url in urls:
        if url not in contents:
            continue
        links = content_to_links(contents[url])
        st = {"url": url, "fetched": len(links), "unique": 0,
              "alive": 0, "gemini": 0}
        order.append(st)
        for i, raw in enumerate(links):
            sig = dedup_signature(raw)
            if sig in seen:
                continue
            seen[sig] = True
            items.append({"raw": raw, "sub": url,
                          "name": link_remark(raw, f"node_{len(items) + 1}")})
            st["unique"] += 1
    return items, order


def load_local_configs(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    links = content_to_links(content)
    label = f"local:{os.path.basename(path)}"
    seen, items = {}, []
    for raw in links:
        sig = dedup_signature(raw)
        if sig in seen:
            continue
        seen[sig] = True
        items.append({"raw": raw, "sub": label,
                      "name": link_remark(raw, f"node_{len(items) + 1}")})
    return items, [{"url": label, "fetched": len(links),
                    "unique": len(items), "alive": 0, "gemini": 0}]


# ---------------------------------------------------------------- testing

_tls = threading.local()
_idx_lock = threading.Lock()
_next_idx = [0]


def worker_index():
    """Stable unique index per thread -> unique SOCKS port & temp file."""
    idx = getattr(_tls, "idx", None)
    if idx is None:
        with _idx_lock:
            idx = _next_idx[0]
            _next_idx[0] += 1
        _tls.idx = idx
    return idx


def curl_text(args, timeout):
    try:
        out = subprocess.run([CURL] + args, capture_output=True,
                             timeout=timeout + 4)
        return out.stdout.decode("utf-8", "ignore")
    except Exception:
        return ""


def curl_run(args, timeout):
    try:
        out = subprocess.run([CURL] + args, capture_output=True,
                             timeout=timeout + 4)
        return out.returncode, out.stdout.decode("utf-8", "ignore")
    except Exception:
        return 1, ""


def quality_battery(port, q, workdir):
    """Stage-3 quality gate on one reused xray inbound:
    1) keep-alive stability + jitter: N tiny transfers on ONE connection
    2) download stall test: sustained throughput must never stall
    3) upload test: POST random bytes (catches broken upload path / Telegram
       stuck on 'Updating...').
    Returns (passed, fail_reason)."""
    socks = ["--socks5-hostname", f"127.0.0.1:{port}"]
    devnull = "NUL" if os.name == "nt" else "/dev/null"

    # 1) keep-alive + jitter (curl reuses the connection across URLs)
    n = q["ka_requests"]
    url1 = "https://speed.cloudflare.com/__down?bytes=1"
    ka_total = n * q["ka_req_timeout"] + 4
    rc, out = curl_run(["-s", "-m", str(q["ka_req_timeout"]), *socks,
                        "-o", devnull, "-w", "%{time_total}\n",
                        *([url1] * n)], ka_total)
    try:
        times = [float(x) for x in out.split() if x]
    except ValueError:
        times = []
    if rc != 0 or len(times) != n:
        return False, "ka"
    spread = max(times) / max(min(times), 0.001)
    if spread > q["ka_spread"]:
        return False, "jitter"

    # 2) download stall test: full file within dl_max, never stalled
    want = q["dl_bytes"]
    rc, out = curl_run(["-s", "-m", str(q["dl_max"]), *socks,
                        "-o", devnull, "-w", "%{size_download}",
                        "--speed-limit", str(q["dl_min_bps"]),
                        "--speed-time", str(q["dl_stall"]),
                        f"https://speed.cloudflare.com/__down?bytes={want}"],
                       q["dl_max"])
    try:
        got = int(out.strip() or 0)
    except ValueError:
        got = 0
    if rc != 0 or got < want * 0.98:
        return False, "dl"

    # 3) upload test
    up_file = os.path.join(workdir, f"up_{port}.bin")
    try:
        if not os.path.isfile(up_file) or os.path.getsize(up_file) != q["up_bytes"]:
            with open(up_file, "wb") as f:
                f.write(os.urandom(q["up_bytes"]))
    except OSError:
        return False, "up"
    rc, out = curl_run(["-s", "-m", str(q["up_max"]), *socks,
                        "-o", devnull, "-w", "%{http_code}",
                        "--data-binary", f"@{up_file}",
                        "-H", "Content-Type: application/octet-stream",
                        "https://speed.cloudflare.com/__up"], q["up_max"])
    if rc != 0 or out.strip() != "200":
        return False, "up"

    return True, ""


def test_config(xray_path, item, base_port, max_latency_ms, allowed,
                gemini_timeout, workdir, qcfg):
    idx = worker_index()
    port = base_port + idx
    cfg_path = os.path.join(workdir, f"xray_w{idx}.json")

    outbound = link_outbound(item["raw"])
    if outbound is None:
        return {**item, "alive": False, "status": "UNSUPPORTED", "ping": 0,
                "loc": "", "ip": "", "gemini": False, "quality_ok": True,
                "q_fail": ""}

    cfg = {
        "log": {"loglevel": "none"},
        "inbounds": [{"port": port, "listen": "127.0.0.1", "protocol": "socks",
                      "settings": {"auth": "noauth", "udp": True}}],
        "outbounds": [outbound, {"protocol": "freedom", "tag": "direct"}],
    }
    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f)

    trace_t = max(3, int(round(max_latency_ms / 1000)))
    res = {**item, "alive": False, "status": "DEAD", "ping": 0, "loc": "",
           "ip": "", "gemini": False, "quality_ok": True, "q_fail": ""}
    proc = None
    try:
        proc = subprocess.Popen([xray_path, "run", "-c", cfg_path],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        time.sleep(0.3)

        t0 = time.time()
        trace = curl_text(["-s", "-m", str(trace_t), "--socks5-hostname",
                           f"127.0.0.1:{port}",
                           "https://www.cloudflare.com/cdn-cgi/trace"], trace_t)
        ping = int((time.time() - t0) * 1000)

        loc = re.search(r"^loc=([A-Z]{2})$", trace, re.M)
        if not loc or ping > max_latency_ms:
            res["status"] = "TIMEOUT" if not loc else "SLOW"
            return res
        ip_m = re.search(r"^ip=(\S+)$", trace, re.M)
        res.update(alive=True, ping=ping, loc=loc.group(1),
                   ip=ip_m.group(1) if ip_m else "")

        if res["loc"] not in allowed:
            res["status"] = "OTHER_COUNTRY"
            return res

        # deep Gemini check: final HTTP status must be 200 (not 403 / error
        # redirect) AND body must be the real app shell without geo-block text
        rc, gout = curl_run(["-s", "-L", "-m", str(gemini_timeout),
                             "--socks5-hostname", f"127.0.0.1:{port}",
                             "-w", "\n__CODE__%{http_code}",
                             "https://gemini.google.com"], gemini_timeout)
        body, _, code = gout.rpartition("__CODE__")
        if (rc == 0 and code.strip() == "200"
                and len(body) > MIN_GEMINI_HTML_LEN
                and not any(pat in body for pat in BLOCKED_PATTERNS)):
            res["gemini"] = True
            res["status"] = "PASS_GEMINI"
        else:
            res["status"] = "GEMINI_BLOCKED"

        # stage 3: quality battery for everything about to enter the sub
        if qcfg["enabled"]:
            q_ok, q_why = quality_battery(port, qcfg, workdir)
            res["quality_ok"] = q_ok
            res["q_fail"] = q_why
            if not q_ok and res["status"] == "PASS_GEMINI":
                res["status"] = "GEMINI_QFAIL"
        return res
    except Exception:
        res["status"] = "ERROR"
        return res
    finally:
        if proc is not None:
            proc.kill()
            try:
                proc.wait(timeout=3)
            except Exception:
                pass
        try:
            os.remove(cfg_path)
        except OSError:
            pass


# ---------------------------------------------------------------- report

def sub_short_name(url):
    m = re.search(r"github(?:usercontent)?\.com/([^/]+)/", url)
    owner = (m.group(1) + "/") if m else ""
    tail = [p for p in url.rstrip("/").split("/") if p]
    return (owner + (tail[-1] if tail else ""))[:42]


def write_report(path, sub_stats, summary, gemini_ok, started, prefix):
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run_link = (f"https://github.com/{repo}/actions/runs/{run_id}"
                if repo and run_id else "_local run_")
    xray_ver = os.environ.get("XRAY_VERSION", "n/a")
    cc = Counter(r["loc"] for r in gemini_ok)
    s = summary

    lines = ["# Github-Gemini — Build Report", ""]
    lines.append(f"- **Run:** {run_link}")
    lines.append(f"- **Date (UTC):** {time.strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"- **Duration:** {int((time.time() - started) / 60)} min")
    lines.append(f"- **Xray core:** {xray_ver}")
    lines += ["", "## Funnel", ""]
    lines.append(f"- **Tested:** {s['tested']} configs — **alive:** {s['alive']} "
                 f"({s['allowed_alive']} in allowed countries, "
                 f"{s['foreign_alive']} in other countries skipped)")
    lines.append(f"- **Gemini-OK:** {s['raw_gemini']} of {s['allowed_alive']} "
                 f"({s['blocked']} Gemini-blocked)")
    if s["qf"]:
        qs = ", ".join(f"{k}={v}" for k, v in
                       sorted(s["qf"].items(), key=lambda x: -x[1]))
        lines.append(f"- **Quality rejects:** {sum(s['qf'].values())} ({qs}) — "
                     f"ka=keep-alive, jitter, dl=download/speed, up=upload")
    lines.append(f"- **In sub:** **{s['in_sub']}** configs = "
                 f"**{s['gemini_in_sub']}** \u264aGemini + "
                 f"**{s['alive_in_sub']}** alive-only "
                 f"(allowed country, no Gemini, passed quality)")
    lines += ["", "## \u264aGemini configs in sub by country", ""]
    if cc:
        lines += ["| Country | Gemini-OK |", "|---|---|"]
        for c, n in cc.most_common():
            lines.append(f"| {c} {flag_of(c)} | {n} |")
    else:
        lines.append("_none_")
    lines += ["", "## Per-subscription performance", "",
              "| # | Subscription | Fetched | Unique | Alive | Gemini OK |",
              "|---|---|---|---|---|---|"]
    for i, st in enumerate(sub_stats, 1):
        lines.append(f"| {i} | {sub_short_name(st['url'])} | {st['fetched']} | "
                     f"{st['unique']} | {st['alive']} | {st['gemini']} |")
    tot = {k: sum(s[k] for s in sub_stats)
           for k in ("fetched", "unique", "alive", "gemini")}
    lines.append(f"| | **TOTAL** | **{tot['fetched']}** | **{tot['unique']}** | "
                 f"**{tot['alive']}** | **{tot['gemini']}** |")
    if repo:
        lines += ["", f"**Subscription:** https://raw.githubusercontent.com/"
                      f"{repo}/main/{prefix}.txt"]
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def git_commit_outputs(prefix):
    """On GitHub Actions, commit and push the generated files. Returns True if
    the remote ended up up-to-date (so the workflow's own commit step no-ops)."""
    if os.environ.get("GITHUB_ACTIONS") != "true":
        return False

    def git(*args):
        return subprocess.run(["git", *args], capture_output=True, text=True)

    files = [f"{prefix}.txt", f"{prefix}-plain.txt", "REPORT.md"]
    git("add", *files)
    if git("diff", "--cached", "--quiet").returncode == 0:
        print("[i] outputs identical to previous run - nothing to commit")
        return True
    msg = (f"[skip ci] update Github-Gemini sub + report "
           f"({time.strftime('%Y-%m-%d %H:%M')} UTC)")
    git("-c", "user.name=github-actions[bot]",
        "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
        "commit", "-m", msg)
    git("pull", "--rebase", "--autostash")
    p = git("push")
    if p.returncode == 0:
        return True
    print(f"[!] git push failed, leaving changes staged for the workflow "
          f"step: {(p.stderr or '').strip()[:200]}")
    git("reset", "--soft", "HEAD~1")
    return False


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Github-Gemini subscription builder")
    ap.add_argument("--settings", default="settings.json")
    ap.add_argument("--configs-file", help="skip downloads; test this local file")
    ap.add_argument("--out-prefix", default="Github-Gemini")
    ap.add_argument("--xray", help="path to xray binary")
    ap.add_argument("--workers", type=int)
    ap.add_argument("--max-configs", type=int)
    ap.add_argument("--dry-run", action="store_true",
                    help="parse + dedup only, no testing")
    args = ap.parse_args()

    settings = {}
    if os.path.isfile(args.settings):
        with open(args.settings, "r", encoding="utf-8") as f:
            settings = json.load(f)

    allowed = set(settings.get("allowed_countries",
                 ["US", "DE", "NL", "CA", "GB", "FR", "TR", "AE", "CH", "NO", "SG"]))
    workers = args.workers or int(settings.get("workers", 24))
    max_latency = int(settings.get("max_latency_ms", 5000))
    gemini_timeout = int(settings.get("gemini_timeout_s", 6))
    base_port = int(settings.get("base_port", 28100))
    max_configs = args.max_configs or int(settings.get("max_configs", 20000))
    budget_min = float(settings.get("runtime_budget_min", 90))
    include_alive = bool(settings.get("include_alive_no_gemini", True))
    qcfg = {
        "enabled":        bool(settings.get("quality_test", True)),
        "ka_requests":    int(settings.get("ka_requests", 6)),
        "ka_req_timeout": int(settings.get("ka_req_timeout", 2)),
        "ka_spread":      float(settings.get("ka_spread", 8)),
        "dl_bytes":       int(settings.get("dl_bytes", 2500000)),
        "dl_min_bps":     int(settings.get("dl_min_bps", 30000)),
        "dl_stall":       int(settings.get("dl_stall_secs", 3)),
        "dl_max":         int(settings.get("dl_max_secs", 12)),
        "up_bytes":       int(settings.get("up_bytes", 524288)),
        "up_max":         int(settings.get("up_max_secs", 10)),
    }

    started = time.time()
    print("=" * 70)
    print("       GITHUB-GEMINI SUBSCRIPTION BUILDER")
    print(f"       workers={workers}  max_latency={max_latency}ms  "
          f"countries={','.join(sorted(allowed))}")
    print("=" * 70, flush=True)

    if args.dry_run:
        args.xray = None  # not needed

    # 1. collect configs
    if args.configs_file:
        items, sub_stats = load_local_configs(args.configs_file)
    else:
        urls = settings.get("subscription_urls", [])
        if not urls:
            print("[!] no subscription_urls in settings and no --configs-file")
            sys.exit(2)
        print(f"[*] downloading {len(urls)} subscriptions ...", flush=True)
        items, sub_stats = download_subs(urls)

    total_unique = len(items)
    if total_unique > max_configs:
        items = items[:max_configs]
    print(f"[+] unique configs: {total_unique}"
          + (f" (testing first {len(items)})" if total_unique > len(items) else ""))

    if args.dry_run:
        ok = sum(1 for it in items if link_outbound(it["raw"]) is not None)
        print(f"[dry-run] parseable: {ok}/{len(items)}  "
              f"unsupported: {len(items) - ok}")
        for st in sub_stats:
            print(f"    {st['url'][:70]:<70} fetched={st['fetched']} unique={st['unique']}")
        sys.exit(0)

    # 2. xray
    xray_path = find_xray(args.xray)
    if not xray_path:
        print("[!] xray binary not found — pass --xray PATH")
        sys.exit(2)
    print(f"[+] xray: {xray_path}")

    workdir = os.path.join(os.environ.get("RUNNER_TEMP", os.environ.get("TEMP", "/tmp")),
                           "gemini_tester")
    os.makedirs(workdir, exist_ok=True)

    # 3. parallel test
    print(f"[*] testing {len(items)} configs with {workers} workers "
          f"(budget {budget_min:.0f} min) ...", flush=True)

    results = []
    deadline = started + budget_min * 60
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(test_config, xray_path, it, base_port, max_latency,
                            allowed, gemini_timeout, workdir, qcfg): it
                for it in items}
        done = 0
        for fut in as_completed(futs):
            done += 1
            res = fut.result()
            results.append(res)
            name = res["name"][:38]
            tag = f"[{done}/{len(items)}]"
            if res["status"] == "PASS_GEMINI":
                tprint(f"{tag} PASS {res['loc']} {res['ping']:>5}ms gemini=OK  {name}")
            elif res["status"] == "GEMINI_QFAIL":
                tprint(f"{tag} QF   {res['loc']} {res['ping']:>5}ms "
                       f"gemini=OK qfail={res['q_fail']}  {name}")
            elif res["status"] == "GEMINI_BLOCKED":
                tprint(f"{tag} blk  {res['loc']} {res['ping']:>5}ms gemini=NO  {name}")
            elif res["status"] == "OTHER_COUNTRY":
                tprint(f"{tag} skip {res['loc']:>2} {res['ping']:>5}ms           {name}")
            elif res["alive"]:
                tprint(f"{tag} slow {res['loc']:>2} {res['ping']:>5}ms           {name}")
            else:
                tprint(f"{tag} dead          --              {name}")
            if time.time() > deadline and done < len(items):
                tprint(f"[!] runtime budget reached — cancelling remaining tests")
                for f2 in futs:
                    f2.cancel()
                break

    # 4. build subscription (quality gate applies to every entry)
    gemini_ok = sorted([r for r in results if r["gemini"] and r["quality_ok"]],
                       key=lambda r: r["ping"])
    alive_only = sorted([r for r in results if r["alive"] and not r["gemini"]
                         and r["loc"] in allowed and r["quality_ok"]],
                        key=lambda r: r["ping"])

    final_links = []
    for r in gemini_ok:
        final_links.append(rename_link(r["raw"], build_prefix(r["loc"], True)
                                       + strip_old_prefix(r["name"])))
    if include_alive:
        for r in alive_only:
            final_links.append(rename_link(r["raw"], build_prefix(r["loc"], False)
                                           + strip_old_prefix(r["name"])))

    # per-sub stats
    by_sub = {st["url"]: st for st in sub_stats}
    for r in results:
        st = by_sub.get(r.get("sub"))
        if not st:
            continue
        if r["alive"]:
            st["alive"] += 1
            if r["gemini"]:
                st["gemini"] += 1

    print()
    print("=" * 80)
    print("  PER-SUBSCRIPTION PERFORMANCE REPORT")
    print("=" * 80)
    alive_count = sum(1 for r in results if r["alive"])
    allowed_alive = [r for r in results if r["alive"] and r["loc"] in allowed]
    raw_gemini = sum(1 for r in results if r["gemini"])
    foreign = alive_count - len(allowed_alive)
    blocked = len(allowed_alive) - raw_gemini
    qf = Counter(r["q_fail"] for r in results
                 if r["alive"] and r["loc"] in allowed and r["q_fail"])
    print(f"  tested={len(results)}  alive={alive_count}  "
          f"(allowed countries: {len(allowed_alive)}, other: {foreign} skipped)")
    print(f"  gemini_ok={raw_gemini}/{len(allowed_alive)}  "
          f"({blocked} gemini-blocked)")
    if qf:
        print("  quality rejects: " + "  ".join(
            f"{k}:{v}" for k, v in qf.most_common()))
    print(f"  IN SUB: {len(final_links)} = {len(gemini_ok)} with "
          f"\u264aGemini + {len(alive_only)} alive-only")
    summary = {
        "tested": len(results),
        "alive": alive_count,
        "allowed_alive": len(allowed_alive),
        "foreign_alive": foreign,
        "raw_gemini": raw_gemini,
        "blocked": blocked,
        "qf": dict(qf),
        "gemini_in_sub": len(gemini_ok),
        "alive_in_sub": len(alive_only),
        "in_sub": len(final_links),
    }
    print(f"  {'#':<3} {'subscription':<42} {'fetched':>7} {'unique':>7} "
          f"{'alive':>6} {'gemini':>6}")
    print("  " + "-" * 78)
    for i, st in enumerate(sub_stats, 1):
        print(f"  {i:<3} {sub_short_name(st['url']):<42} {st['fetched']:>7} "
              f"{st['unique']:>7} {st['alive']:>6} {st['gemini']:>6}")
    tot = {k: sum(s[k] for s in sub_stats)
           for k in ("fetched", "unique", "alive", "gemini")}
    print("  " + "-" * 78)
    print(f"  {'ALL':<3} {'OVERALL TOTALS':<42} {tot['fetched']:>7} "
          f"{tot['unique']:>7} {tot['alive']:>6} {tot['gemini']:>6}")
    cc = Counter(r["loc"] for r in gemini_ok)
    if cc:
        print("  Gemini-OK by country: " + "  ".join(
            f"{c}:{n}" for c, n in cc.most_common()))

    # 5. write outputs (UTF-8, no BOM, LF)
    if final_links:
        plain = os.path.abspath(f"{args.out_prefix}-plain.txt")
        b64_file = os.path.abspath(f"{args.out_prefix}.txt")
        with open(plain, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(final_links) + "\n")
        blob = base64.b64encode("\n".join(final_links).encode("utf-8")).decode()
        with open(b64_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(blob + "\n")
        print()
        print(f"[+] wrote {len(final_links)} configs:")
        print(f"    {b64_file}")
        print(f"    {plain}")
        report_path = os.path.abspath("REPORT.md")
        write_report(report_path, sub_stats, summary, gemini_ok,
                     started, args.out_prefix)
        print(f"    {report_path}")
        if git_commit_outputs(args.out_prefix):
            print("[+] outputs committed to the repository")
        repo = os.environ.get("GITHUB_REPOSITORY")
        if repo:
            print(f"    sub link: https://raw.githubusercontent.com/{repo}/main/{args.out_prefix}.txt")
            print(f"    jsDelivr: https://cdn.jsdelivr.net/gh/{repo}@main/{args.out_prefix}.txt")
        print(f"[*] total runtime: {int((time.time() - started) / 60)} min")
        sys.exit(0)

    print(f"[!] zero configs passed — keeping previous sub "
          f"(no output written). runtime: {int((time.time() - started) / 60)} min")
    sys.exit(3)


if __name__ == "__main__":
    main()
