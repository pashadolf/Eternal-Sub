# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/40314295822
- **Date (UTC):** 2026-10-26 11:29
- **Duration:** 9 min
- **Xray core:** v26.10.21

## Funnel

- **No-fingerprint excluded:** 4890 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 6332 configs — **alive:** 1954 (1325 in allowed countries, 629 in other countries skipped)
- **Gemini-OK:** 1024 of 1325 (301 Gemini-blocked)
- **Quality rejects:** 280 (jitter=162, dl=74, ka=26, up=18) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **863** configs = **863** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 182 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 402 |
| NL 🇳🇱 | 146 |
| FR 🇫🇷 | 88 |
| SG 🇸🇬 | 79 |
| DE 🇩🇪 | 62 |
| GB 🇬🇧 | 61 |
| TR 🇹🇷 | 19 |
| CH 🇨🇭 | 6 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 284 | 173 | 67 | 35 |
| 2 | miladtahanian/sub.txt | 207 | 115 | 11 | 3 |
| 3 | rtwo2/top.txt | 1000 | 737 | 246 | 110 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 166 | 61 | 24 | 8 |
| 5 | roosterkid/V2RAY_RAW.txt | 125 | 50 | 20 | 6 |
| 6 | MahanKenway/vless.txt | 150 | 10 | 1 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 97 | 21 | 7 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 152 | 123 | 91 | 79 |
| 11 | Au1rxx/v2ray-base64.txt | 1364 | 916 | 765 | 411 |
| 12 | 0xRadikal/configs.txt | 1139 | 341 | 195 | 115 |
| 13 | configs_base64.txt | 4572 | 532 | 66 | 37 |
| 14 | F0rc3Run/proxies.txt | 370 | 116 | 65 | 28 |
| 15 | Delta-Kronecker/vless.txt | 1249 | 696 | 187 | 95 |
| 16 | ermaozi/v2ray.txt | 417 | 172 | 4 | 1 |
| 17 | ninjastrikers/all.txt | 2588 | 553 | 66 | 28 |
| 18 | Farid-Karimi/mixed_iran.txt | 382 | 161 | 44 | 12 |
| 19 | liketolivefree/sub.txt | 425 | 289 | 18 | 6 |
| 20 | roosterkid/V2RAY_BASE64.txt | 125 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 379 | 89 | 3 | 3 |
| 22 | barry-far/Sub4.txt | 500 | 184 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1479 | 766 | 60 | 40 |
| 24 | Mosifree/Reality | 240 | 113 | 0 | 0 |
| | **TOTAL** | **17476** | **6332** | **1954** | **1024** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
