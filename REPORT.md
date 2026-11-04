# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41903795738
- **Date (UTC):** 2026-11-04 20:12
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7663 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5392 configs — **alive:** 325 (221 in allowed countries, 104 in other countries skipped)
- **Gemini-OK:** 147 of 221 (74 Gemini-blocked)
- **Quality rejects:** 81 (jitter=27, dl=27, up=15, ka=12) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **111** configs = **111** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 29 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 30 |
| NL 🇳🇱 | 27 |
| GB 🇬🇧 | 24 |
| DE 🇩🇪 | 15 |
| FR 🇫🇷 | 6 |
| TR 🇹🇷 | 4 |
| NO 🇳🇴 | 2 |
| SG 🇸🇬 | 2 |
| CH 🇨🇭 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 634 | 325 | 63 | 23 |
| 2 | miladtahanian/sub.txt | 116 | 19 | 1 | 1 |
| 3 | rtwo2/top.txt | 1000 | 510 | 65 | 29 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 136 | 47 | 6 | 1 |
| 5 | roosterkid/V2RAY_RAW.txt | 118 | 25 | 6 | 1 |
| 6 | MahanKenway/vless.txt | 139 | 14 | 1 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 58 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 108 | 11 | 4 | 4 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 238 | 40 | 12 |
| 12 | 0xRadikal/configs.txt | 855 | 168 | 82 | 50 |
| 13 | configs_base64.txt | 4951 | 435 | 13 | 7 |
| 14 | F0rc3Run/proxies.txt | 50 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 781 | 322 | 21 | 11 |
| 16 | ermaozi/v2ray.txt | 53 | 31 | 0 | 0 |
| 17 | ninjastrikers/all.txt | 2573 | 421 | 17 | 5 |
| 18 | Farid-Karimi/mixed_iran.txt | 647 | 107 | 1 | 1 |
| 19 | liketolivefree/sub.txt | 209 | 108 | 2 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 118 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 401 | 76 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 94 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1624 | 540 | 1 | 0 |
| 24 | Mosifree/Reality | 266 | 122 | 0 | 0 |
| | **TOTAL** | **22502** | **5862** | **325** | **147** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
