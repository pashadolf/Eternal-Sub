# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/40201749083
- **Date (UTC):** 2026-10-25 14:28
- **Duration:** 7 min
- **Xray core:** v26.10.21

## Funnel

- **No-fingerprint excluded:** 4705 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 6350 configs — **alive:** 1882 (1289 in allowed countries, 593 in other countries skipped)
- **Gemini-OK:** 1048 of 1289 (241 Gemini-blocked)
- **Quality rejects:** 283 (jitter=184, dl=73, ka=19, up=7) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **876** configs = **876** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 130 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 443 |
| NL 🇳🇱 | 134 |
| GB 🇬🇧 | 77 |
| FR 🇫🇷 | 76 |
| DE 🇩🇪 | 70 |
| SG 🇸🇬 | 61 |
| TR 🇹🇷 | 10 |
| CH 🇨🇭 | 5 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 256 | 137 | 35 | 14 |
| 2 | miladtahanian/sub.txt | 391 | 283 | 2 | 0 |
| 3 | rtwo2/top.txt | 1000 | 731 | 277 | 133 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 146 | 75 | 21 | 8 |
| 5 | roosterkid/V2RAY_RAW.txt | 122 | 6 | 1 | 1 |
| 6 | MahanKenway/vless.txt | 137 | 12 | 2 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 97 | 24 | 7 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 185 | 129 | 107 | 102 |
| 11 | Au1rxx/v2ray-base64.txt | 1340 | 852 | 715 | 426 |
| 12 | 0xRadikal/configs.txt | 1007 | 325 | 208 | 120 |
| 13 | configs_base64.txt | 4366 | 452 | 40 | 20 |
| 14 | F0rc3Run/proxies.txt | 239 | 61 | 28 | 14 |
| 15 | Delta-Kronecker/vless.txt | 1273 | 795 | 193 | 102 |
| 16 | ermaozi/v2ray.txt | 400 | 186 | 19 | 9 |
| 17 | ninjastrikers/all.txt | 2594 | 552 | 70 | 24 |
| 18 | Farid-Karimi/mixed_iran.txt | 357 | 192 | 58 | 21 |
| 19 | liketolivefree/sub.txt | 425 | 289 | 18 | 6 |
| 20 | roosterkid/V2RAY_BASE64.txt | 122 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 383 | 90 | 2 | 2 |
| 22 | barry-far/Sub4.txt | 500 | 197 | 6 | 2 |
| 23 | 10ium/merged_base64 | 1479 | 744 | 56 | 37 |
| 24 | Mosifree/Reality | 240 | 107 | 0 | 0 |
| | **TOTAL** | **17125** | **6350** | **1882** | **1048** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
