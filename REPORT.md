# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/43877809612
- **Date (UTC):** 2026-11-16 13:42
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7838 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5475 configs — **alive:** 380 (274 in allowed countries, 106 in other countries skipped)
- **Gemini-OK:** 123 of 274 (151 Gemini-blocked)
- **Quality rejects:** 84 (jitter=40, dl=22, ka=14, up=8) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 2 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **93** configs = **90** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 98 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| SG 🇸🇬 | 22 |
| US 🇺🇸 | 21 |
| DE 🇩🇪 | 13 |
| NL 🇳🇱 | 12 |
| SE 🇸🇪 | 6 |
| FR 🇫🇷 | 5 |
| CH 🇨🇭 | 4 |
| FI 🇫🇮 | 3 |
| TR 🇹🇷 | 3 |
| GB 🇬🇧 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 171 | 95 | 29 | 17 |
| 2 | miladtahanian/sub.txt | 107 | 55 | 6 | 2 |
| 3 | rtwo2/top.txt | 1000 | 521 | 92 | 28 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 135 | 60 | 16 | 3 |
| 5 | roosterkid/V2RAY_RAW.txt | 62 | 9 | 0 | 0 |
| 6 | MahanKenway/vless.txt | 125 | 54 | 2 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 67 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 76 | 10 | 4 | 2 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 396 | 41 | 20 |
| 12 | 0xRadikal/configs.txt | 983 | 256 | 138 | 35 |
| 13 | configs_base64.txt | 5533 | 470 | 5 | 0 |
| 14 | F0rc3Run/proxies.txt | 35 | 1 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 848 | 249 | 26 | 9 |
| 16 | ermaozi/v2ray.txt | 375 | 192 | 4 | 2 |
| 17 | ninjastrikers/all.txt | 2493 | 372 | 14 | 5 |
| 18 | Farid-Karimi/mixed_iran.txt | 403 | 86 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 164 | 72 | 1 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 62 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 365 | 70 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 75 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1557 | 547 | 1 | 0 |
| 24 | Mosifree/Reality | 266 | 118 | 0 | 0 |
| | **TOTAL** | **22471** | **5960** | **380** | **123** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
