# Github-Gemini — Build Report

- **Run:** https://github.com/pourih/Eternal-Sub/actions/runs/40901385060
- **Date (UTC):** 2026-10-29 15:29
- **Duration:** 4 min
- **Xray core:** v26.10.29

## Funnel

- **No-fingerprint excluded:** 8202 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4087 configs — **alive:** 625 (428 in allowed countries, 197 in other countries skipped)
- **Gemini-OK:** 310 of 428 (118 Gemini-blocked)
- **Quality rejects:** 107 (jitter=67, dl=27, ka=9, up=4) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **253** configs = **253** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 68 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 130 |
| NL 🇳🇱 | 43 |
| SG 🇸🇬 | 27 |
| DE 🇩🇪 | 23 |
| GB 🇬🇧 | 12 |
| FR 🇫🇷 | 11 |
| TR 🇹🇷 | 4 |
| CH 🇨🇭 | 3 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 288 | 170 | 54 | 22 |
| 2 | miladtahanian/sub.txt | 155 | 43 | 12 | 1 |
| 3 | rtwo2/top.txt | 1000 | 522 | 165 | 81 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 148 | 57 | 9 | 4 |
| 5 | roosterkid/V2RAY_RAW.txt | 120 | 8 | 1 | 1 |
| 6 | MahanKenway/vless.txt | 152 | 9 | 2 | 2 |
| 7 | luckylukam/configs_tested.txt | 125 | 82 | 9 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 173 | 37 | 13 | 13 |
| 11 | Au1rxx/v2ray-base64.txt | 1405 | 301 | 191 | 104 |
| 12 | 0xRadikal/configs.txt | 987 | 145 | 59 | 31 |
| 13 | configs_base64.txt | 4764 | 526 | 26 | 10 |
| 14 | F0rc3Run/proxies.txt | 49 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 894 | 354 | 32 | 23 |
| 16 | ermaozi/v2ray.txt | 389 | 169 | 10 | 1 |
| 17 | ninjastrikers/all.txt | 2503 | 431 | 24 | 3 |
| 18 | Farid-Karimi/mixed_iran.txt | 502 | 86 | 4 | 2 |
| 19 | liketolivefree/sub.txt | 425 | 192 | 0 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 120 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 385 | 71 | 1 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 187 | 1 | 1 |
| 23 | 10ium/merged_base64 | 1454 | 491 | 12 | 10 |
| 24 | Mosifree/Reality | 266 | 168 | 0 | 0 |
| | **TOTAL** | **16842** | **4087** | **625** | **310** |

**Subscription:** https://raw.githubusercontent.com/pourih/Eternal-Sub/main/Github-Gemini.txt
