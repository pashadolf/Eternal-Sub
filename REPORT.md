# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42468253401
- **Date (UTC):** 2026-11-08 09:46
- **Duration:** 4 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7203 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5411 configs — **alive:** 400 (286 in allowed countries, 114 in other countries skipped)
- **Gemini-OK:** 69 of 286 (217 Gemini-blocked)
- **Quality rejects:** 86 (jitter=51, dl=23, ka=12) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **48** configs = **45** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 155 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 15 |
| DE 🇩🇪 | 10 |
| GB 🇬🇧 | 9 |
| NL 🇳🇱 | 4 |
| FI 🇫🇮 | 3 |
| SG 🇸🇬 | 2 |
| CH 🇨🇭 | 1 |
| SE 🇸🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 641 | 307 | 60 | 12 |
| 2 | miladtahanian/sub.txt | 79 | 13 | 1 | 0 |
| 3 | rtwo2/top.txt | 1000 | 497 | 66 | 10 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 157 | 59 | 7 | 0 |
| 5 | roosterkid/V2RAY_RAW.txt | 75 | 6 | 3 | 1 |
| 6 | MahanKenway/vless.txt | 130 | 7 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 60 | 3 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2183 | 0 | 0 |
| 10 | iampedii/base64.txt | 161 | 13 | 6 | 2 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 252 | 43 | 3 |
| 12 | 0xRadikal/configs.txt | 1137 | 262 | 121 | 18 |
| 13 | configs_base64.txt | 5240 | 493 | 13 | 6 |
| 14 | Delta-Kronecker/vless.txt | 979 | 514 | 70 | 17 |
| 15 | liketolivefree/sub.txt | 209 | 127 | 3 | 0 |
| 16 | roosterkid/V2RAY_BASE64.txt | 75 | 0 | 0 | 0 |
| 17 | MhdiTaheri/mix.txt | 384 | 86 | 0 | 0 |
| 18 | barry-far/Sub4.txt | 500 | 191 | 0 | 0 |
| 19 | 10ium/merged_base64 | 1680 | 645 | 4 | 0 |
| 20 | Mosifree/Reality | 266 | 119 | 0 | 0 |
| | **TOTAL** | **19936** | **5840** | **400** | **69** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
