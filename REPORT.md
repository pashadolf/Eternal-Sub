# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/44319225937
- **Date (UTC):** 2026-11-18 14:02
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7855 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5576 configs — **alive:** 286 (222 in allowed countries, 64 in other countries skipped)
- **Gemini-OK:** 100 of 222 (122 Gemini-blocked)
- **Quality rejects:** 72 (jitter=32, dl=20, ka=14, up=6) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 4 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **60** configs = **60** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 86 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 14 |
| SG 🇸🇬 | 14 |
| NL 🇳🇱 | 12 |
| DE 🇩🇪 | 7 |
| SE 🇸🇪 | 5 |
| FI 🇫🇮 | 4 |
| FR 🇫🇷 | 3 |
| TR 🇹🇷 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 189 | 89 | 16 | 9 |
| 2 | miladtahanian/sub.txt | 121 | 51 | 5 | 2 |
| 3 | rtwo2/top.txt | 1000 | 545 | 66 | 29 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 134 | 43 | 5 | 0 |
| 5 | roosterkid/V2RAY_RAW.txt | 75 | 15 | 2 | 2 |
| 6 | MahanKenway/vless.txt | 122 | 44 | 3 | 2 |
| 7 | luckylukam/configs_tested.txt | 125 | 73 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 117 | 13 | 5 | 2 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 404 | 25 | 15 |
| 12 | 0xRadikal/configs.txt | 895 | 191 | 100 | 27 |
| 13 | configs_base64.txt | 5593 | 510 | 9 | 1 |
| 14 | F0rc3Run/proxies.txt | 57 | 1 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 795 | 318 | 28 | 8 |
| 16 | ermaozi/v2ray.txt | 330 | 171 | 1 | 0 |
| 17 | ninjastrikers/all.txt | 2457 | 387 | 13 | 1 |
| 18 | Farid-Karimi/mixed_iran.txt | 612 | 182 | 4 | 0 |
| 19 | liketolivefree/sub.txt | 164 | 78 | 2 | 2 |
| 20 | roosterkid/V2RAY_BASE64.txt | 75 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 361 | 71 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 65 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1572 | 535 | 1 | 0 |
| 24 | Mosifree/Reality | 266 | 122 | 0 | 0 |
| | **TOTAL** | **22646** | **6093** | **286** | **100** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
