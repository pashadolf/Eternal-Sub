# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/40490812029
- **Date (UTC):** 2026-10-27 10:53
- **Duration:** 9 min
- **Xray core:** v26.10.21

## Funnel

- **No-fingerprint excluded:** 5095 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 6396 configs — **alive:** 1983 (1336 in allowed countries, 647 in other countries skipped)
- **Gemini-OK:** 982 of 1336 (354 Gemini-blocked)
- **Quality rejects:** 244 (jitter=127, dl=76, ka=22, up=19) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **857** configs = **857** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 235 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 419 |
| NL 🇳🇱 | 140 |
| FR 🇫🇷 | 89 |
| DE 🇩🇪 | 64 |
| SG 🇸🇬 | 62 |
| GB 🇬🇧 | 51 |
| TR 🇹🇷 | 20 |
| CH 🇨🇭 | 12 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 282 | 175 | 67 | 29 |
| 2 | miladtahanian/sub.txt | 217 | 105 | 3 | 0 |
| 3 | rtwo2/top.txt | 1000 | 730 | 258 | 119 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 153 | 70 | 17 | 6 |
| 5 | roosterkid/V2RAY_RAW.txt | 128 | 31 | 17 | 9 |
| 6 | MahanKenway/vless.txt | 155 | 16 | 4 | 2 |
| 7 | luckylukam/configs_tested.txt | 125 | 100 | 19 | 7 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 199 | 134 | 94 | 80 |
| 11 | Au1rxx/v2ray-base64.txt | 1466 | 938 | 772 | 407 |
| 12 | 0xRadikal/configs.txt | 1296 | 375 | 202 | 90 |
| 13 | configs_base64.txt | 4775 | 653 | 90 | 39 |
| 14 | F0rc3Run/proxies.txt | 370 | 120 | 68 | 32 |
| 15 | Delta-Kronecker/vless.txt | 1222 | 605 | 186 | 80 |
| 16 | ermaozi/v2ray.txt | 391 | 180 | 3 | 1 |
| 17 | ninjastrikers/all.txt | 2603 | 491 | 52 | 21 |
| 18 | Farid-Karimi/mixed_iran.txt | 489 | 212 | 49 | 15 |
| 19 | liketolivefree/sub.txt | 425 | 308 | 20 | 7 |
| 20 | roosterkid/V2RAY_BASE64.txt | 128 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 398 | 87 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 174 | 1 | 0 |
| 23 | 10ium/merged_base64 | 1486 | 743 | 60 | 37 |
| 24 | Mosifree/Reality | 240 | 111 | 0 | 0 |
| | **TOTAL** | **18086** | **6396** | **1983** | **982** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
