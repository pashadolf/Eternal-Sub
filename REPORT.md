# Github-Gemini — Build Report

- **Run:** https://github.com/pourih/Eternal-Sub/actions/runs/40903682448
- **Date (UTC):** 2026-10-29 15:42
- **Duration:** 3 min
- **Xray core:** v26.10.29

## Funnel

- **No-fingerprint excluded:** 8215 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 3911 configs — **alive:** 570 (390 in allowed countries, 180 in other countries skipped)
- **Gemini-OK:** 302 of 390 (88 Gemini-blocked)
- **Quality rejects:** 97 (jitter=71, dl=13, ka=9, up=4) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **234** configs = **234** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 59 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 103 |
| NL 🇳🇱 | 44 |
| DE 🇩🇪 | 25 |
| SG 🇸🇬 | 24 |
| FR 🇫🇷 | 21 |
| GB 🇬🇧 | 11 |
| CH 🇨🇭 | 3 |
| TR 🇹🇷 | 3 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 288 | 170 | 56 | 27 |
| 2 | miladtahanian/sub.txt | 155 | 43 | 12 | 5 |
| 3 | rtwo2/top.txt | 1000 | 488 | 150 | 78 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 148 | 57 | 9 | 4 |
| 5 | roosterkid/V2RAY_RAW.txt | 120 | 8 | 2 | 2 |
| 6 | MahanKenway/vless.txt | 152 | 9 | 2 | 2 |
| 7 | luckylukam/configs_tested.txt | 125 | 82 | 10 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 173 | 36 | 13 | 12 |
| 11 | Au1rxx/v2ray-base64.txt | 1405 | 256 | 149 | 79 |
| 12 | 0xRadikal/configs.txt | 977 | 136 | 52 | 21 |
| 13 | configs_base64.txt | 4774 | 496 | 20 | 9 |
| 14 | F0rc3Run/proxies.txt | 49 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 894 | 357 | 45 | 37 |
| 16 | ermaozi/v2ray.txt | 389 | 167 | 10 | 0 |
| 17 | ninjastrikers/all.txt | 2503 | 424 | 21 | 12 |
| 18 | Farid-Karimi/mixed_iran.txt | 502 | 74 | 5 | 2 |
| 19 | liketolivefree/sub.txt | 425 | 179 | 0 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 120 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 385 | 70 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 183 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1454 | 470 | 13 | 10 |
| 24 | Mosifree/Reality | 266 | 168 | 0 | 0 |
| | **TOTAL** | **16842** | **3911** | **570** | **302** |

**Subscription:** https://raw.githubusercontent.com/pourih/Eternal-Sub/main/Github-Gemini.txt
