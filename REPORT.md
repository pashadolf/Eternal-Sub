# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42359910673
- **Date (UTC):** 2026-11-07 09:32
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7746 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5550 configs — **alive:** 339 (245 in allowed countries, 94 in other countries skipped)
- **Gemini-OK:** 148 of 245 (97 Gemini-blocked)
- **Quality rejects:** 102 (jitter=44, ka=30, dl=19, up=9) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **110** configs = **108** ♊Gemini + **2** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 35 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 27 |
| US 🇺🇸 | 20 |
| GB 🇬🇧 | 19 |
| DE 🇩🇪 | 14 |
| FR 🇫🇷 | 9 |
| TR 🇹🇷 | 5 |
| CA 🇨🇦 | 4 |
| SG 🇸🇬 | 4 |
| CH 🇨🇭 | 2 |
| FI 🇫🇮 | 2 |
| SE 🇸🇪 | 1 |
| AU 🇦🇺 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 653 | 332 | 54 | 27 |
| 2 | miladtahanian/sub.txt | 74 | 21 | 1 | 1 |
| 3 | rtwo2/top.txt | 1000 | 473 | 59 | 13 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 46 | 3 | 1 |
| 5 | roosterkid/V2RAY_RAW.txt | 69 | 11 | 5 | 3 |
| 6 | MahanKenway/vless.txt | 140 | 10 | 1 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 58 | 1 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2183 | 0 | 0 |
| 10 | iampedii/base64.txt | 155 | 8 | 2 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 248 | 38 | 11 |
| 12 | 0xRadikal/configs.txt | 959 | 173 | 107 | 77 |
| 13 | configs_base64.txt | 5072 | 477 | 6 | 3 |
| 14 | F0rc3Run/proxies.txt | 35 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 830 | 432 | 41 | 8 |
| 16 | ermaozi/v2ray.txt | 332 | 165 | 2 | 1 |
| 17 | ninjastrikers/all.txt | 2537 | 348 | 17 | 1 |
| 18 | Farid-Karimi/mixed_iran.txt | 556 | 118 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 209 | 113 | 2 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 69 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 379 | 76 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 126 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1554 | 508 | 0 | 0 |
| 24 | Mosifree/Reality | 266 | 111 | 0 | 0 |
| | **TOTAL** | **22762** | **6043** | **339** | **148** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
