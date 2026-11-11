# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/43022790550
- **Date (UTC):** 2026-11-11 12:46
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7771 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5709 configs — **alive:** 386 (233 in allowed countries, 153 in other countries skipped)
- **Gemini-OK:** 137 of 233 (96 Gemini-blocked)
- **Quality rejects:** 87 (jitter=40, dl=34, ka=11, up=2) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 1 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **90** configs = **87** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 58 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 19 |
| SG 🇸🇬 | 18 |
| DE 🇩🇪 | 13 |
| GB 🇬🇧 | 12 |
| NL 🇳🇱 | 11 |
| CA 🇨🇦 | 5 |
| FR 🇫🇷 | 5 |
| AU 🇦🇺 | 2 |
| SE 🇸🇪 | 1 |
| FI 🇫🇮 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 662 | 333 | 57 | 26 |
| 2 | miladtahanian/sub.txt | 128 | 64 | 12 | 5 |
| 3 | rtwo2/top.txt | 1000 | 506 | 82 | 22 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 138 | 35 | 3 | 1 |
| 5 | roosterkid/V2RAY_RAW.txt | 72 | 8 | 0 | 0 |
| 6 | MahanKenway/vless.txt | 149 | 13 | 1 | 1 |
| 7 | luckylukam/configs_tested.txt | 125 | 60 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 14 | 14 | 8 | 7 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 110 | 7 | 0 | 0 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 252 | 37 | 16 |
| 12 | 0xRadikal/configs.txt | 1000 | 214 | 129 | 43 |
| 13 | configs_base64.txt | 5313 | 503 | 11 | 5 |
| 14 | F0rc3Run/proxies.txt | 52 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 714 | 273 | 27 | 6 |
| 16 | ermaozi/v2ray.txt | 372 | 174 | 2 | 1 |
| 17 | ninjastrikers/all.txt | 2535 | 379 | 8 | 2 |
| 18 | Farid-Karimi/mixed_iran.txt | 261 | 45 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 209 | 119 | 3 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 72 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 394 | 76 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 152 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1602 | 610 | 4 | 1 |
| 24 | Mosifree/Reality | 266 | 117 | 0 | 0 |
| | **TOTAL** | **22774** | **6139** | **386** | **137** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
