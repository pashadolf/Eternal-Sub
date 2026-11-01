# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41304055129
- **Date (UTC):** 2026-11-01 12:04
- **Duration:** 8 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 8083 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 8192 configs — **alive:** 1898 (1380 in allowed countries, 518 in other countries skipped)
- **Gemini-OK:** 895 of 1380 (485 Gemini-blocked)
- **Quality rejects:** 309 (jitter=205, dl=71, ka=23, up=10) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **792** configs = **792** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 279 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 439 |
| NL 🇳🇱 | 140 |
| DE 🇩🇪 | 75 |
| FR 🇫🇷 | 49 |
| SG 🇸🇬 | 36 |
| CH 🇨🇭 | 22 |
| GB 🇬🇧 | 19 |
| TR 🇹🇷 | 10 |
| AE 🇦🇪 | 2 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 641 | 362 | 155 | 85 |
| 2 | miladtahanian/sub.txt | 243 | 143 | 18 | 8 |
| 3 | rtwo2/top.txt | 1000 | 658 | 263 | 116 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 57 | 23 | 15 |
| 5 | roosterkid/V2RAY_RAW.txt | 143 | 22 | 8 | 2 |
| 6 | MahanKenway/vless.txt | 140 | 20 | 7 | 5 |
| 7 | luckylukam/configs_tested.txt | 125 | 95 | 24 | 9 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2198 | 0 | 0 |
| 10 | iampedii/base64.txt | 111 | 32 | 25 | 24 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 634 | 516 | 292 |
| 12 | 0xRadikal/configs.txt | 1767 | 650 | 327 | 89 |
| 13 | configs_base64.txt | 5133 | 452 | 21 | 8 |
| 14 | F0rc3Run/proxies.txt | 62 | 1 | 1 | 1 |
| 15 | Delta-Kronecker/vless.txt | 1577 | 724 | 164 | 87 |
| 16 | ermaozi/v2ray.txt | 56 | 17 | 1 | 0 |
| 17 | ninjastrikers/all.txt | 2604 | 601 | 137 | 50 |
| 18 | Farid-Karimi/mixed_iran.txt | 584 | 264 | 85 | 31 |
| 19 | liketolivefree/sub.txt | 209 | 149 | 57 | 37 |
| 20 | roosterkid/V2RAY_BASE64.txt | 143 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 373 | 83 | 2 | 2 |
| 22 | barry-far/Sub4.txt | 500 | 164 | 3 | 0 |
| 23 | 10ium/merged_base64 | 1535 | 694 | 61 | 34 |
| 24 | Mosifree/Reality | 266 | 160 | 0 | 0 |
| | **TOTAL** | **24460** | **8192** | **1898** | **895** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
