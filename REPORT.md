# Github-Gemini — Build Report

- **Run:** https://github.com/pourih/Eternal-Sub/actions/runs/40892680670
- **Date (UTC):** 2026-10-29 14:38
- **Duration:** 4 min
- **Xray core:** v26.10.29

## Funnel

- **No-fingerprint excluded:** 8261 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4201 configs — **alive:** 729 (494 in allowed countries, 235 in other countries skipped)
- **Gemini-OK:** 363 of 494 (131 Gemini-blocked)
- **Quality rejects:** 115 (jitter=50, dl=32, ka=25, up=8) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **307** configs = **307** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 72 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 154 |
| NL 🇳🇱 | 54 |
| FR 🇫🇷 | 28 |
| SG 🇸🇬 | 23 |
| DE 🇩🇪 | 22 |
| GB 🇬🇧 | 12 |
| CH 🇨🇭 | 8 |
| TR 🇹🇷 | 6 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 288 | 170 | 59 | 24 |
| 2 | miladtahanian/sub.txt | 155 | 46 | 12 | 4 |
| 3 | rtwo2/top.txt | 1000 | 532 | 180 | 93 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 148 | 58 | 8 | 5 |
| 5 | roosterkid/V2RAY_RAW.txt | 120 | 5 | 1 | 0 |
| 6 | MahanKenway/vless.txt | 152 | 9 | 2 | 2 |
| 7 | luckylukam/configs_tested.txt | 125 | 84 | 11 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 173 | 57 | 33 | 28 |
| 11 | Au1rxx/v2ray-base64.txt | 1415 | 313 | 213 | 116 |
| 12 | 0xRadikal/configs.txt | 1049 | 175 | 67 | 32 |
| 13 | configs_base64.txt | 4774 | 495 | 18 | 7 |
| 14 | F0rc3Run/proxies.txt | 49 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 894 | 365 | 46 | 16 |
| 16 | ermaozi/v2ray.txt | 389 | 169 | 11 | 1 |
| 17 | ninjastrikers/all.txt | 2506 | 482 | 43 | 17 |
| 18 | Farid-Karimi/mixed_iran.txt | 498 | 77 | 7 | 4 |
| 19 | liketolivefree/sub.txt | 425 | 203 | 4 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 120 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 385 | 71 | 1 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 191 | 1 | 1 |
| 23 | 10ium/merged_base64 | 1454 | 495 | 12 | 11 |
| 24 | Mosifree/Reality | 266 | 166 | 0 | 0 |
| | **TOTAL** | **16923** | **4201** | **729** | **363** |

**Subscription:** https://raw.githubusercontent.com/pourih/Eternal-Sub/main/Github-Gemini.txt
