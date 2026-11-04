# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41835432688
- **Date (UTC):** 2026-11-04 13:16
- **Duration:** 7 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7834 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 7073 configs — **alive:** 1241 (901 in allowed countries, 340 in other countries skipped)
- **Gemini-OK:** 718 of 901 (183 Gemini-blocked)
- **Quality rejects:** 197 (jitter=86, dl=54, ka=42, up=15) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **629** configs = **629** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 75 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 234 |
| NL 🇳🇱 | 167 |
| DE 🇩🇪 | 70 |
| SG 🇸🇬 | 51 |
| FR 🇫🇷 | 48 |
| GB 🇬🇧 | 38 |
| TR 🇹🇷 | 13 |
| CH 🇨🇭 | 8 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 651 | 364 | 150 | 76 |
| 2 | miladtahanian/sub.txt | 116 | 26 | 6 | 3 |
| 3 | rtwo2/top.txt | 1000 | 652 | 193 | 110 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 133 | 56 | 15 | 10 |
| 5 | roosterkid/V2RAY_RAW.txt | 97 | 41 | 25 | 13 |
| 6 | MahanKenway/vless.txt | 138 | 20 | 10 | 9 |
| 7 | luckylukam/configs_tested.txt | 125 | 96 | 15 | 5 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2199 | 0 | 0 |
| 10 | iampedii/base64.txt | 123 | 67 | 48 | 46 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 651 | 205 | 126 |
| 12 | 0xRadikal/configs.txt | 880 | 263 | 175 | 110 |
| 13 | configs_base64.txt | 5045 | 504 | 41 | 23 |
| 14 | F0rc3Run/proxies.txt | 69 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 781 | 463 | 132 | 60 |
| 16 | ermaozi/v2ray.txt | 53 | 43 | 4 | 0 |
| 17 | ninjastrikers/all.txt | 2519 | 602 | 89 | 45 |
| 18 | Farid-Karimi/mixed_iran.txt | 645 | 248 | 52 | 21 |
| 19 | liketolivefree/sub.txt | 209 | 176 | 27 | 16 |
| 20 | roosterkid/V2RAY_BASE64.txt | 97 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 398 | 91 | 5 | 5 |
| 22 | barry-far/Sub4.txt | 500 | 107 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1616 | 775 | 49 | 40 |
| 24 | Mosifree/Reality | 266 | 169 | 0 | 0 |
| | **TOTAL** | **22559** | **7625** | **1241** | **718** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
