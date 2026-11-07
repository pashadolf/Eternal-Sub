# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42357815634
- **Date (UTC):** 2026-11-07 09:03
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7747 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5565 configs — **alive:** 342 (228 in allowed countries, 114 in other countries skipped)
- **Gemini-OK:** 113 of 228 (115 Gemini-blocked)
- **Quality rejects:** 105 (jitter=57, dl=27, ka=17, up=4) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **78** configs = **78** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 45 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 27 |
| US 🇺🇸 | 14 |
| DE 🇩🇪 | 13 |
| TR 🇹🇷 | 8 |
| FR 🇫🇷 | 7 |
| GB 🇬🇧 | 4 |
| SG 🇸🇬 | 3 |
| CH 🇨🇭 | 2 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 653 | 332 | 58 | 20 |
| 2 | miladtahanian/sub.txt | 74 | 21 | 0 | 0 |
| 3 | rtwo2/top.txt | 1000 | 473 | 57 | 11 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 46 | 4 | 1 |
| 5 | roosterkid/V2RAY_RAW.txt | 68 | 10 | 1 | 0 |
| 6 | MahanKenway/vless.txt | 140 | 10 | 1 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 58 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2183 | 0 | 0 |
| 10 | iampedii/base64.txt | 155 | 9 | 4 | 2 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 248 | 42 | 8 |
| 12 | 0xRadikal/configs.txt | 985 | 191 | 107 | 41 |
| 13 | configs_base64.txt | 5090 | 487 | 11 | 2 |
| 14 | F0rc3Run/proxies.txt | 35 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 830 | 422 | 37 | 24 |
| 16 | ermaozi/v2ray.txt | 332 | 166 | 2 | 1 |
| 17 | ninjastrikers/all.txt | 2537 | 348 | 13 | 2 |
| 18 | Farid-Karimi/mixed_iran.txt | 556 | 118 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 209 | 113 | 2 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 68 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 379 | 76 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 126 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1554 | 509 | 2 | 1 |
| 24 | Mosifree/Reality | 266 | 111 | 0 | 0 |
| | **TOTAL** | **22804** | **6063** | **342** | **113** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
