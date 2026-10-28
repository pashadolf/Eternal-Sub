# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/40680172472
- **Date (UTC):** 2026-10-28 11:37
- **Duration:** 9 min
- **Xray core:** v26.10.21

## Funnel

- **No-fingerprint excluded:** 4983 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 6080 configs — **alive:** 1943 (1329 in allowed countries, 614 in other countries skipped)
- **Gemini-OK:** 968 of 1329 (361 Gemini-blocked)
- **Quality rejects:** 351 (jitter=191, dl=101, ka=39, up=20) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **764** configs = **764** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 214 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 361 |
| NL 🇳🇱 | 153 |
| FR 🇫🇷 | 78 |
| SG 🇸🇬 | 71 |
| DE 🇩🇪 | 47 |
| GB 🇬🇧 | 26 |
| CH 🇨🇭 | 15 |
| TR 🇹🇷 | 12 |
| AE 🇦🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 299 | 191 | 77 | 39 |
| 2 | miladtahanian/sub.txt | 182 | 69 | 6 | 3 |
| 3 | rtwo2/top.txt | 1000 | 714 | 238 | 118 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 146 | 67 | 30 | 14 |
| 5 | roosterkid/V2RAY_RAW.txt | 125 | 25 | 13 | 3 |
| 6 | MahanKenway/vless.txt | 145 | 17 | 4 | 3 |
| 7 | luckylukam/configs_tested.txt | 125 | 98 | 21 | 8 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 167 | 111 | 80 | 60 |
| 11 | Au1rxx/v2ray-base64.txt | 1473 | 913 | 726 | 396 |
| 12 | 0xRadikal/configs.txt | 1141 | 316 | 217 | 102 |
| 13 | configs_base64.txt | 4709 | 657 | 98 | 51 |
| 14 | F0rc3Run/proxies.txt | 406 | 145 | 57 | 13 |
| 15 | Delta-Kronecker/vless.txt | 1132 | 557 | 190 | 76 |
| 16 | ermaozi/v2ray.txt | 58 | 31 | 3 | 1 |
| 17 | ninjastrikers/all.txt | 2604 | 528 | 66 | 24 |
| 18 | Farid-Karimi/mixed_iran.txt | 477 | 198 | 39 | 14 |
| 19 | liketolivefree/sub.txt | 425 | 302 | 18 | 4 |
| 20 | roosterkid/V2RAY_BASE64.txt | 125 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 379 | 84 | 2 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 199 | 8 | 7 |
| 23 | 10ium/merged_base64 | 1496 | 709 | 50 | 31 |
| 24 | Mosifree/Reality | 240 | 111 | 0 | 0 |
| | **TOTAL** | **17392** | **6080** | **1943** | **968** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
