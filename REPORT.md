# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/43230437080
- **Date (UTC):** 2026-11-12 13:50
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7832 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5726 configs — **alive:** 347 (218 in allowed countries, 129 in other countries skipped)
- **Gemini-OK:** 97 of 218 (121 Gemini-blocked)
- **Quality rejects:** 75 (jitter=37, dl=19, ka=15, up=4) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 1 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **74** configs = **71** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 71 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 23 |
| SG 🇸🇬 | 15 |
| DE 🇩🇪 | 11 |
| NL 🇳🇱 | 10 |
| AU 🇦🇺 | 3 |
| CA 🇨🇦 | 2 |
| GB 🇬🇧 | 2 |
| FR 🇫🇷 | 2 |
| FI 🇫🇮 | 1 |
| TR 🇹🇷 | 1 |
| AE 🇦🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 193 | 101 | 28 | 16 |
| 2 | miladtahanian/sub.txt | 143 | 56 | 0 | 0 |
| 3 | rtwo2/top.txt | 1000 | 527 | 85 | 14 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 131 | 53 | 6 | 2 |
| 5 | roosterkid/V2RAY_RAW.txt | 76 | 5 | 0 | 0 |
| 6 | MahanKenway/vless.txt | 147 | 63 | 5 | 1 |
| 7 | luckylukam/configs_tested.txt | 125 | 61 | 0 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 132 | 7 | 3 | 3 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 403 | 42 | 20 |
| 12 | 0xRadikal/configs.txt | 1027 | 227 | 106 | 22 |
| 13 | configs_base64.txt | 5366 | 467 | 15 | 3 |
| 14 | F0rc3Run/proxies.txt | 53 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 748 | 318 | 30 | 8 |
| 16 | ermaozi/v2ray.txt | 379 | 207 | 1 | 0 |
| 17 | ninjastrikers/all.txt | 2508 | 359 | 10 | 3 |
| 18 | Farid-Karimi/mixed_iran.txt | 539 | 144 | 11 | 2 |
| 19 | liketolivefree/sub.txt | 209 | 119 | 2 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 76 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 386 | 78 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 155 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1607 | 590 | 3 | 3 |
| 24 | Mosifree/Reality | 266 | 116 | 0 | 0 |
| | **TOTAL** | **22697** | **6241** | **347** | **97** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
