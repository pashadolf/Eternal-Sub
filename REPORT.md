# Github-Gemini — Build Report

- **Run:** https://github.com/pourih/Eternal-Sub/actions/runs/40905680440
- **Date (UTC):** 2026-10-29 15:54
- **Duration:** 3 min
- **Xray core:** v26.10.29

## Funnel

- **No-fingerprint excluded:** 8227 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 3645 configs — **alive:** 366 (231 in allowed countries, 135 in other countries skipped)
- **Gemini-OK:** 160 of 231 (71 Gemini-blocked)
- **Quality rejects:** 68 (jitter=33, dl=20, ka=12, up=3) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **126** configs = **126** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 37 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 41 |
| NL 🇳🇱 | 28 |
| DE 🇩🇪 | 23 |
| FR 🇫🇷 | 9 |
| TR 🇹🇷 | 8 |
| SG 🇸🇬 | 8 |
| GB 🇬🇧 | 7 |
| CH 🇨🇭 | 2 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 288 | 170 | 55 | 26 |
| 2 | miladtahanian/sub.txt | 155 | 28 | 1 | 1 |
| 3 | rtwo2/top.txt | 1000 | 454 | 112 | 49 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 148 | 56 | 5 | 3 |
| 5 | roosterkid/V2RAY_RAW.txt | 120 | 8 | 1 | 1 |
| 6 | MahanKenway/vless.txt | 152 | 6 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 82 | 8 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 173 | 35 | 13 | 13 |
| 11 | Au1rxx/v2ray-base64.txt | 1405 | 146 | 60 | 20 |
| 12 | 0xRadikal/configs.txt | 1004 | 130 | 52 | 29 |
| 13 | configs_base64.txt | 4732 | 450 | 9 | 0 |
| 14 | F0rc3Run/proxies.txt | 49 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 894 | 364 | 29 | 13 |
| 16 | ermaozi/v2ray.txt | 389 | 163 | 8 | 0 |
| 17 | ninjastrikers/all.txt | 2503 | 401 | 7 | 0 |
| 18 | Farid-Karimi/mixed_iran.txt | 502 | 67 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 425 | 178 | 0 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 120 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 385 | 66 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 179 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1454 | 456 | 6 | 4 |
| 24 | Mosifree/Reality | 266 | 168 | 0 | 0 |
| | **TOTAL** | **16827** | **3645** | **366** | **160** |

**Subscription:** https://raw.githubusercontent.com/pourih/Eternal-Sub/main/Github-Gemini.txt
