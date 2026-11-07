# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42358832843
- **Date (UTC):** 2026-11-07 09:17
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7744 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5568 configs — **alive:** 351 (253 in allowed countries, 98 in other countries skipped)
- **Gemini-OK:** 166 of 253 (87 Gemini-blocked)
- **Quality rejects:** 105 (jitter=61, dl=22, ka=19, up=3) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **107** configs = **107** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 41 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 28 |
| US 🇺🇸 | 20 |
| GB 🇬🇧 | 16 |
| DE 🇩🇪 | 14 |
| TR 🇹🇷 | 8 |
| FR 🇫🇷 | 6 |
| FI 🇫🇮 | 5 |
| SG 🇸🇬 | 4 |
| CA 🇨🇦 | 2 |
| AU 🇦🇺 | 2 |
| CH 🇨🇭 | 2 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 653 | 332 | 57 | 25 |
| 2 | miladtahanian/sub.txt | 74 | 21 | 0 | 0 |
| 3 | rtwo2/top.txt | 1000 | 473 | 56 | 11 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 46 | 4 | 2 |
| 5 | roosterkid/V2RAY_RAW.txt | 69 | 11 | 4 | 2 |
| 6 | MahanKenway/vless.txt | 140 | 10 | 1 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 58 | 1 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2183 | 0 | 0 |
| 10 | iampedii/base64.txt | 155 | 8 | 3 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 248 | 42 | 8 |
| 12 | 0xRadikal/configs.txt | 994 | 189 | 116 | 86 |
| 13 | configs_base64.txt | 5090 | 490 | 9 | 1 |
| 14 | F0rc3Run/proxies.txt | 35 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 830 | 422 | 37 | 25 |
| 16 | ermaozi/v2ray.txt | 332 | 166 | 1 | 1 |
| 17 | ninjastrikers/all.txt | 2537 | 347 | 17 | 3 |
| 18 | Farid-Karimi/mixed_iran.txt | 556 | 119 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 209 | 113 | 3 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 69 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 379 | 76 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 126 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1554 | 510 | 0 | 0 |
| 24 | Mosifree/Reality | 266 | 111 | 0 | 0 |
| | **TOTAL** | **22815** | **6065** | **351** | **166** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
