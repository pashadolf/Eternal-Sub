# Github-Gemini — Build Report

- **Run:** https://github.com/pourih/Eternal-Sub/actions/runs/40888487317
- **Date (UTC):** 2026-10-29 14:13
- **Duration:** 4 min
- **Xray core:** v26.10.29

## Funnel

- **No-fingerprint excluded:** 8276 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4310 configs — **alive:** 865 (606 in allowed countries, 259 in other countries skipped)
- **Gemini-OK:** 456 of 606 (150 Gemini-blocked)
- **Quality rejects:** 151 (jitter=93, dl=32, ka=21, up=5) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **366** configs = **366** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 89 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 168 |
| NL 🇳🇱 | 73 |
| DE 🇩🇪 | 35 |
| FR 🇫🇷 | 34 |
| SG 🇸🇬 | 27 |
| GB 🇬🇧 | 16 |
| CH 🇨🇭 | 8 |
| TR 🇹🇷 | 5 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 288 | 170 | 61 | 27 |
| 2 | miladtahanian/sub.txt | 155 | 46 | 11 | 5 |
| 3 | rtwo2/top.txt | 1000 | 544 | 193 | 102 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 148 | 58 | 10 | 5 |
| 5 | roosterkid/V2RAY_RAW.txt | 120 | 6 | 3 | 2 |
| 6 | MahanKenway/vless.txt | 152 | 9 | 2 | 2 |
| 7 | luckylukam/configs_tested.txt | 125 | 84 | 11 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 173 | 78 | 54 | 48 |
| 11 | Au1rxx/v2ray-base64.txt | 1411 | 379 | 273 | 141 |
| 12 | 0xRadikal/configs.txt | 1038 | 146 | 72 | 31 |
| 13 | configs_base64.txt | 4774 | 479 | 18 | 6 |
| 14 | F0rc3Run/proxies.txt | 49 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 894 | 401 | 79 | 50 |
| 16 | ermaozi/v2ray.txt | 389 | 175 | 11 | 2 |
| 17 | ninjastrikers/all.txt | 2506 | 489 | 39 | 17 |
| 18 | Farid-Karimi/mixed_iran.txt | 498 | 77 | 7 | 4 |
| 19 | liketolivefree/sub.txt | 425 | 203 | 4 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 120 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 385 | 71 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 193 | 1 | 1 |
| 23 | 10ium/merged_base64 | 1454 | 498 | 15 | 10 |
| 24 | Mosifree/Reality | 266 | 166 | 0 | 0 |
| | **TOTAL** | **16908** | **4310** | **865** | **456** |

**Subscription:** https://raw.githubusercontent.com/pourih/Eternal-Sub/main/Github-Gemini.txt
