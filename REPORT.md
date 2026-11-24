# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/45430712346
- **Date (UTC):** 2026-11-24 15:56
- **Duration:** 2 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7720 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5031 configs — **alive:** 157 (114 in allowed countries, 43 in other countries skipped)
- **Gemini-OK:** 83 of 114 (31 Gemini-blocked)
- **Quality rejects:** 33 (jitter=12, dl=11, ka=9, up=1) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 3 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **60** configs = **60** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 18 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 19 |
| SG 🇸🇬 | 15 |
| US 🇺🇸 | 7 |
| DE 🇩🇪 | 6 |
| CH 🇨🇭 | 3 |
| FI 🇫🇮 | 3 |
| FR 🇫🇷 | 3 |
| SE 🇸🇪 | 2 |
| GB 🇬🇧 | 1 |
| AU 🇦🇺 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 122 | 53 | 11 | 7 |
| 2 | miladtahanian/sub.txt | 128 | 72 | 0 | 0 |
| 3 | rtwo2/top.txt | 1000 | 560 | 45 | 24 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 154 | 64 | 6 | 4 |
| 5 | roosterkid/V2RAY_RAW.txt | 34 | 0 | 0 | 0 |
| 6 | MahanKenway/vless.txt | 133 | 55 | 2 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 73 | 0 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 72 | 4 | 1 | 0 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 423 | 31 | 23 |
| 12 | 0xRadikal/configs.txt | 571 | 91 | 31 | 15 |
| 13 | configs_base64.txt | 5628 | 459 | 10 | 3 |
| 14 | F0rc3Run/proxies.txt | 113 | 4 | 0 | 0 |
| 15 | ermaozi/v2ray.txt | 198 | 84 | 1 | 0 |
| 16 | ninjastrikers/all.txt | 2346 | 356 | 14 | 5 |
| 17 | Farid-Karimi/mixed_iran.txt | 163 | 71 | 3 | 1 |
| 18 | liketolivefree/sub.txt | 156 | 86 | 0 | 0 |
| 19 | roosterkid/V2RAY_BASE64.txt | 34 | 0 | 0 | 0 |
| 20 | MhdiTaheri/mix.txt | 343 | 71 | 0 | 0 |
| 21 | barry-far/Sub4.txt | 342 | 19 | 0 | 0 |
| 22 | 10ium/merged_base64 | 1453 | 524 | 2 | 1 |
| 23 | Mosifree/Reality | 266 | 124 | 0 | 0 |
| | **TOTAL** | **20467** | **5378** | **157** | **83** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
