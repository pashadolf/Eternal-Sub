# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/43715386498
- **Date (UTC):** 2026-11-15 12:48
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7885 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5632 configs — **alive:** 282 (217 in allowed countries, 65 in other countries skipped)
- **Gemini-OK:** 117 of 217 (100 Gemini-blocked)
- **Quality rejects:** 81 (jitter=30, dl=27, ka=21, up=3) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 3 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **75** configs = **73** ♊Gemini + **2** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 60 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 19 |
| DE 🇩🇪 | 16 |
| SG 🇸🇬 | 12 |
| NL 🇳🇱 | 8 |
| FR 🇫🇷 | 5 |
| SE 🇸🇪 | 5 |
| GB 🇬🇧 | 3 |
| CA 🇨🇦 | 2 |
| FI 🇫🇮 | 1 |
| TR 🇹🇷 | 1 |
| CH 🇨🇭 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 199 | 109 | 31 | 13 |
| 2 | miladtahanian/sub.txt | 76 | 1 | 0 | 0 |
| 3 | rtwo2/top.txt | 1000 | 497 | 67 | 25 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 130 | 46 | 4 | 4 |
| 5 | roosterkid/V2RAY_RAW.txt | 77 | 14 | 2 | 1 |
| 6 | MahanKenway/vless.txt | 137 | 53 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 67 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 123 | 19 | 1 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 397 | 38 | 22 |
| 12 | 0xRadikal/configs.txt | 858 | 170 | 80 | 30 |
| 13 | configs_base64.txt | 5510 | 529 | 13 | 5 |
| 14 | F0rc3Run/proxies.txt | 37 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 920 | 452 | 32 | 14 |
| 16 | ermaozi/v2ray.txt | 344 | 161 | 1 | 0 |
| 17 | ninjastrikers/all.txt | 2465 | 373 | 11 | 1 |
| 18 | Farid-Karimi/mixed_iran.txt | 400 | 89 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 164 | 77 | 1 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 77 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 366 | 77 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 82 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1539 | 554 | 0 | 0 |
| 24 | Mosifree/Reality | 266 | 121 | 0 | 0 |
| | **TOTAL** | **22399** | **6073** | **282** | **117** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
