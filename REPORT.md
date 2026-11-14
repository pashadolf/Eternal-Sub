# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/43593608121
- **Date (UTC):** 2026-11-14 12:15
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7862 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5496 configs — **alive:** 281 (226 in allowed countries, 55 in other countries skipped)
- **Gemini-OK:** 108 of 226 (118 Gemini-blocked)
- **Quality rejects:** 61 (jitter=40, dl=11, ka=8, up=2) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 1 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **89** configs = **86** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 78 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 34 |
| SG 🇸🇬 | 12 |
| DE 🇩🇪 | 10 |
| FR 🇫🇷 | 8 |
| NL 🇳🇱 | 7 |
| GB 🇬🇧 | 4 |
| FI 🇫🇮 | 4 |
| SE 🇸🇪 | 2 |
| TR 🇹🇷 | 2 |
| BE 🇧🇪 | 1 |
| CH 🇨🇭 | 1 |
| AE 🇦🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 170 | 101 | 26 | 13 |
| 2 | miladtahanian/sub.txt | 179 | 91 | 0 | 0 |
| 3 | rtwo2/top.txt | 1000 | 506 | 85 | 30 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 137 | 52 | 4 | 2 |
| 5 | roosterkid/V2RAY_RAW.txt | 60 | 10 | 0 | 0 |
| 6 | MahanKenway/vless.txt | 138 | 53 | 4 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 66 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 81 | 2 | 1 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 396 | 32 | 18 |
| 12 | 0xRadikal/configs.txt | 895 | 167 | 80 | 26 |
| 13 | configs_base64.txt | 5461 | 484 | 12 | 5 |
| 14 | F0rc3Run/proxies.txt | 52 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 613 | 233 | 16 | 4 |
| 16 | ermaozi/v2ray.txt | 344 | 177 | 0 | 0 |
| 17 | ninjastrikers/all.txt | 2463 | 355 | 8 | 4 |
| 18 | Farid-Karimi/mixed_iran.txt | 494 | 106 | 2 | 1 |
| 19 | liketolivefree/sub.txt | 164 | 65 | 1 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 60 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 385 | 81 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 78 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1610 | 592 | 9 | 4 |
| 24 | Mosifree/Reality | 266 | 120 | 0 | 0 |
| | **TOTAL** | **22283** | **5920** | **281** | **108** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
