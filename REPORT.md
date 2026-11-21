# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/44909028418
- **Date (UTC):** 2026-11-21 13:31
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7917 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5385 configs — **alive:** 239 (191 in allowed countries, 48 in other countries skipped)
- **Gemini-OK:** 109 of 191 (82 Gemini-blocked)
- **Quality rejects:** 60 (jitter=30, dl=13, ka=12, up=5) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 4 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **77** configs = **77** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 50 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| SG 🇸🇬 | 18 |
| NL 🇳🇱 | 17 |
| DE 🇩🇪 | 15 |
| US 🇺🇸 | 13 |
| CA 🇨🇦 | 4 |
| FR 🇫🇷 | 3 |
| GB 🇬🇧 | 2 |
| SE 🇸🇪 | 2 |
| CH 🇨🇭 | 2 |
| FI 🇫🇮 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 152 | 64 | 16 | 9 |
| 2 | miladtahanian/sub.txt | 126 | 35 | 2 | 0 |
| 3 | rtwo2/top.txt | 1000 | 525 | 57 | 37 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 149 | 61 | 12 | 2 |
| 5 | roosterkid/V2RAY_RAW.txt | 54 | 6 | 1 | 0 |
| 6 | MahanKenway/vless.txt | 104 | 43 | 3 | 2 |
| 7 | luckylukam/configs_tested.txt | 125 | 72 | 1 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 89 | 3 | 2 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 409 | 30 | 18 |
| 12 | 0xRadikal/configs.txt | 836 | 177 | 72 | 25 |
| 13 | configs_base64.txt | 5651 | 532 | 11 | 5 |
| 14 | F0rc3Run/proxies.txt | 91 | 7 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 700 | 245 | 16 | 5 |
| 16 | ermaozi/v2ray.txt | 234 | 110 | 0 | 0 |
| 17 | ninjastrikers/all.txt | 2388 | 336 | 9 | 3 |
| 18 | Farid-Karimi/mixed_iran.txt | 592 | 167 | 2 | 0 |
| 19 | liketolivefree/sub.txt | 156 | 59 | 2 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 54 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 382 | 76 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 401 | 10 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1650 | 603 | 3 | 0 |
| 24 | Mosifree/Reality | 266 | 118 | 0 | 0 |
| | **TOTAL** | **22286** | **5843** | **239** | **109** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
