# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/45027068842
- **Date (UTC):** 2026-11-22 13:25
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7878 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5488 configs — **alive:** 236 (171 in allowed countries, 65 in other countries skipped)
- **Gemini-OK:** 95 of 171 (76 Gemini-blocked)
- **Quality rejects:** 66 (jitter=29, ka=19, dl=12, up=6) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **69** configs = **69** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 36 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 19 |
| SG 🇸🇬 | 16 |
| DE 🇩🇪 | 14 |
| NL 🇳🇱 | 9 |
| FR 🇫🇷 | 6 |
| GB 🇬🇧 | 2 |
| CH 🇨🇭 | 1 |
| SE 🇸🇪 | 1 |
| FI 🇫🇮 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 155 | 85 | 18 | 10 |
| 2 | miladtahanian/sub.txt | 118 | 41 | 2 | 0 |
| 3 | rtwo2/top.txt | 1000 | 555 | 68 | 30 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 146 | 51 | 7 | 1 |
| 5 | roosterkid/V2RAY_RAW.txt | 38 | 6 | 0 | 0 |
| 6 | MahanKenway/vless.txt | 137 | 51 | 1 | 1 |
| 7 | luckylukam/configs_tested.txt | 125 | 73 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 106 | 12 | 5 | 4 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 407 | 25 | 18 |
| 12 | 0xRadikal/configs.txt | 811 | 125 | 50 | 18 |
| 13 | configs_base64.txt | 5708 | 542 | 11 | 0 |
| 14 | F0rc3Run/proxies.txt | 84 | 5 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 623 | 194 | 20 | 4 |
| 16 | ermaozi/v2ray.txt | 234 | 114 | 3 | 1 |
| 17 | ninjastrikers/all.txt | 2427 | 389 | 17 | 5 |
| 18 | Farid-Karimi/mixed_iran.txt | 589 | 182 | 3 | 2 |
| 19 | liketolivefree/sub.txt | 156 | 71 | 1 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 38 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 351 | 74 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 259 | 8 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1644 | 664 | 3 | 0 |
| 24 | Mosifree/Reality | 266 | 120 | 0 | 0 |
| | **TOTAL** | **22101** | **5954** | **236** | **95** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
