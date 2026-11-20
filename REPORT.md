# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/44749331403
- **Date (UTC):** 2026-11-20 14:03
- **Duration:** 2 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7914 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5451 configs — **alive:** 176 (137 in allowed countries, 39 in other countries skipped)
- **Gemini-OK:** 73 of 137 (64 Gemini-blocked)
- **Quality rejects:** 44 (jitter=29, ka=8, dl=6, up=1) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 3 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **53** configs = **53** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 37 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| SG 🇸🇬 | 15 |
| NL 🇳🇱 | 14 |
| US 🇺🇸 | 8 |
| DE 🇩🇪 | 7 |
| FR 🇫🇷 | 4 |
| TR 🇹🇷 | 2 |
| SE 🇸🇪 | 1 |
| FI 🇫🇮 | 1 |
| CA 🇨🇦 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 158 | 64 | 12 | 4 |
| 2 | miladtahanian/sub.txt | 86 | 8 | 0 | 0 |
| 3 | rtwo2/top.txt | 1000 | 540 | 44 | 17 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 144 | 62 | 6 | 3 |
| 5 | roosterkid/V2RAY_RAW.txt | 45 | 2 | 0 | 0 |
| 6 | MahanKenway/vless.txt | 115 | 53 | 4 | 1 |
| 7 | luckylukam/configs_tested.txt | 125 | 72 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 100 | 4 | 4 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 405 | 24 | 18 |
| 12 | 0xRadikal/configs.txt | 694 | 110 | 39 | 19 |
| 13 | configs_base64.txt | 5677 | 577 | 8 | 1 |
| 14 | F0rc3Run/proxies.txt | 35 | 1 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 623 | 251 | 19 | 7 |
| 16 | ermaozi/v2ray.txt | 260 | 127 | 7 | 1 |
| 17 | ninjastrikers/all.txt | 2452 | 410 | 6 | 0 |
| 18 | Farid-Karimi/mixed_iran.txt | 619 | 178 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 164 | 92 | 2 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 54 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 369 | 76 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 469 | 61 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1641 | 563 | 0 | 0 |
| 24 | Mosifree/Reality | 266 | 121 | 0 | 0 |
| | **TOTAL** | **22182** | **5962** | **176** | **73** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
