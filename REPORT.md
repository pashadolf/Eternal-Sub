# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/43430900094
- **Date (UTC):** 2026-11-13 13:10
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7821 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5539 configs — **alive:** 322 (236 in allowed countries, 86 in other countries skipped)
- **Gemini-OK:** 150 of 236 (86 Gemini-blocked)
- **Quality rejects:** 86 (jitter=51, dl=23, ka=11, up=1) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **99** configs = **96** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 54 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 20 |
| US 🇺🇸 | 18 |
| SG 🇸🇬 | 16 |
| DE 🇩🇪 | 14 |
| FR 🇫🇷 | 8 |
| GB 🇬🇧 | 6 |
| FI 🇫🇮 | 3 |
| AU 🇦🇺 | 3 |
| CH 🇨🇭 | 2 |
| SE 🇸🇪 | 2 |
| TR 🇹🇷 | 2 |
| CA 🇨🇦 | 1 |
| AE 🇦🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 209 | 121 | 36 | 22 |
| 2 | miladtahanian/sub.txt | 162 | 107 | 13 | 4 |
| 3 | rtwo2/top.txt | 1000 | 512 | 60 | 26 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 131 | 50 | 4 | 2 |
| 5 | roosterkid/V2RAY_RAW.txt | 78 | 10 | 1 | 1 |
| 6 | MahanKenway/vless.txt | 133 | 59 | 2 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 64 | 1 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 148 | 31 | 9 | 5 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 393 | 51 | 29 |
| 12 | 0xRadikal/configs.txt | 989 | 192 | 88 | 40 |
| 13 | configs_base64.txt | 5413 | 462 | 12 | 4 |
| 14 | F0rc3Run/proxies.txt | 48 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 675 | 251 | 24 | 12 |
| 16 | ermaozi/v2ray.txt | 353 | 165 | 1 | 1 |
| 17 | ninjastrikers/all.txt | 2484 | 375 | 16 | 3 |
| 18 | Farid-Karimi/mixed_iran.txt | 455 | 86 | 1 | 0 |
| 19 | liketolivefree/sub.txt | 164 | 60 | 3 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 78 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 366 | 78 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 110 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1565 | 548 | 0 | 0 |
| 24 | Mosifree/Reality | 266 | 119 | 0 | 0 |
| | **TOTAL** | **22428** | **5978** | **322** | **150** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
