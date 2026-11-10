# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42824861666
- **Date (UTC):** 2026-11-10 13:32
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7864 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5556 configs — **alive:** 389 (285 in allowed countries, 104 in other countries skipped)
- **Gemini-OK:** 123 of 285 (162 Gemini-blocked)
- **Quality rejects:** 110 (jitter=73, dl=18, ka=17, up=2) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **81** configs = **78** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 97 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| DE 🇩🇪 | 15 |
| SG 🇸🇬 | 15 |
| US 🇺🇸 | 14 |
| NL 🇳🇱 | 13 |
| GB 🇬🇧 | 11 |
| SE 🇸🇪 | 3 |
| FR 🇫🇷 | 2 |
| AU 🇦🇺 | 2 |
| CA 🇨🇦 | 1 |
| FI 🇫🇮 | 1 |
| CH 🇨🇭 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 664 | 331 | 46 | 21 |
| 2 | miladtahanian/sub.txt | 136 | 49 | 4 | 1 |
| 3 | rtwo2/top.txt | 1000 | 467 | 73 | 15 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 142 | 46 | 6 | 1 |
| 5 | roosterkid/V2RAY_RAW.txt | 82 | 13 | 3 | 1 |
| 6 | MahanKenway/vless.txt | 142 | 9 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 58 | 2 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2184 | 0 | 0 |
| 10 | iampedii/base64.txt | 105 | 22 | 3 | 0 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 248 | 36 | 14 |
| 12 | 0xRadikal/configs.txt | 1078 | 275 | 147 | 40 |
| 13 | configs_base64.txt | 5294 | 440 | 14 | 8 |
| 14 | F0rc3Run/proxies.txt | 55 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 735 | 247 | 38 | 17 |
| 16 | ermaozi/v2ray.txt | 388 | 144 | 0 | 0 |
| 17 | ninjastrikers/all.txt | 2440 | 347 | 11 | 2 |
| 18 | Farid-Karimi/mixed_iran.txt | 263 | 49 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 209 | 123 | 3 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 82 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 380 | 77 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 499 | 151 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1588 | 592 | 3 | 2 |
| 24 | Mosifree/Reality | 266 | 119 | 0 | 0 |
| | **TOTAL** | **22771** | **5997** | **389** | **123** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
