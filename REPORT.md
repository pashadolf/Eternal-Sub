# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41639699150
- **Date (UTC):** 2026-11-03 13:02
- **Duration:** 7 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 8120 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 7291 configs — **alive:** 1363 (960 in allowed countries, 403 in other countries skipped)
- **Gemini-OK:** 777 of 960 (183 Gemini-blocked)
- **Quality rejects:** 189 (jitter=105, dl=50, ka=29, up=5) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **665** configs = **665** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 106 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 272 |
| NL 🇳🇱 | 158 |
| DE 🇩🇪 | 69 |
| SG 🇸🇬 | 57 |
| FR 🇫🇷 | 51 |
| GB 🇬🇧 | 31 |
| TR 🇹🇷 | 20 |
| CH 🇨🇭 | 7 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 672 | 385 | 169 | 82 |
| 2 | miladtahanian/sub.txt | 88 | 13 | 3 | 3 |
| 3 | rtwo2/top.txt | 1000 | 650 | 211 | 113 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 144 | 64 | 26 | 10 |
| 5 | roosterkid/V2RAY_RAW.txt | 147 | 42 | 28 | 11 |
| 6 | MahanKenway/vless.txt | 141 | 24 | 10 | 7 |
| 7 | luckylukam/configs_tested.txt | 125 | 94 | 18 | 6 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2199 | 0 | 0 |
| 10 | iampedii/base64.txt | 167 | 81 | 62 | 55 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 661 | 249 | 170 |
| 12 | 0xRadikal/configs.txt | 982 | 276 | 178 | 101 |
| 13 | configs_base64.txt | 4960 | 433 | 15 | 11 |
| 14 | F0rc3Run/proxies.txt | 64 | 3 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 781 | 434 | 142 | 82 |
| 16 | ermaozi/v2ray.txt | 443 | 155 | 3 | 2 |
| 17 | ninjastrikers/all.txt | 2488 | 589 | 98 | 41 |
| 18 | Farid-Karimi/mixed_iran.txt | 734 | 330 | 66 | 23 |
| 19 | liketolivefree/sub.txt | 209 | 161 | 29 | 17 |
| 20 | roosterkid/V2RAY_BASE64.txt | 147 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 373 | 92 | 6 | 5 |
| 22 | barry-far/Sub4.txt | 500 | 178 | 2 | 2 |
| 23 | 10ium/merged_base64 | 1630 | 798 | 48 | 36 |
| 24 | Mosifree/Reality | 266 | 169 | 0 | 0 |
| | **TOTAL** | **23159** | **7843** | **1363** | **777** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
