# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42035307571
- **Date (UTC):** 2026-11-05 13:27
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7695 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5503 configs — **alive:** 367 (248 in allowed countries, 119 in other countries skipped)
- **Gemini-OK:** 117 of 248 (131 Gemini-blocked)
- **Quality rejects:** 101 (jitter=30, dl=30, up=22, ka=19) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **96** configs = **96** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 51 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 35 |
| NL 🇳🇱 | 22 |
| DE 🇩🇪 | 16 |
| GB 🇬🇧 | 10 |
| TR 🇹🇷 | 5 |
| FR 🇫🇷 | 4 |
| CH 🇨🇭 | 2 |
| SG 🇸🇬 | 1 |
| NO 🇳🇴 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 610 | 310 | 72 | 27 |
| 2 | miladtahanian/sub.txt | 115 | 35 | 11 | 3 |
| 3 | rtwo2/top.txt | 999 | 522 | 77 | 9 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 33 | 6 | 3 |
| 5 | roosterkid/V2RAY_RAW.txt | 120 | 26 | 9 | 2 |
| 6 | MahanKenway/vless.txt | 142 | 7 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 58 | 2 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 126 | 35 | 8 | 4 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 243 | 44 | 6 |
| 12 | 0xRadikal/configs.txt | 1046 | 202 | 81 | 45 |
| 13 | configs_base64.txt | 5068 | 414 | 8 | 1 |
| 14 | F0rc3Run/proxies.txt | 55 | 2 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 719 | 237 | 28 | 5 |
| 16 | ermaozi/v2ray.txt | 391 | 229 | 0 | 0 |
| 17 | ninjastrikers/all.txt | 2583 | 350 | 8 | 2 |
| 18 | Farid-Karimi/mixed_iran.txt | 554 | 97 | 3 | 0 |
| 19 | liketolivefree/sub.txt | 209 | 107 | 1 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 120 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 371 | 75 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 82 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1624 | 593 | 8 | 8 |
| 24 | Mosifree/Reality | 266 | 123 | 0 | 0 |
| | **TOTAL** | **22991** | **5971** | **367** | **117** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
