# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41419146244
- **Date (UTC):** 2026-11-02 09:22
- **Duration:** 6 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7888 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 7468 configs — **alive:** 1411 (996 in allowed countries, 415 in other countries skipped)
- **Gemini-OK:** 761 of 996 (235 Gemini-blocked)
- **Quality rejects:** 255 (jitter=184, dl=41, ka=23, up=7) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **596** configs = **596** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 145 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 231 |
| NL 🇳🇱 | 167 |
| DE 🇩🇪 | 62 |
| SG 🇸🇬 | 55 |
| FR 🇫🇷 | 39 |
| TR 🇹🇷 | 17 |
| GB 🇬🇧 | 13 |
| CH 🇨🇭 | 12 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 649 | 378 | 165 | 84 |
| 2 | miladtahanian/sub.txt | 106 | 40 | 3 | 1 |
| 3 | rtwo2/top.txt | 1000 | 669 | 269 | 132 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 62 | 16 | 7 |
| 5 | roosterkid/V2RAY_RAW.txt | 148 | 18 | 13 | 6 |
| 6 | MahanKenway/vless.txt | 138 | 26 | 11 | 10 |
| 7 | luckylukam/configs_tested.txt | 125 | 93 | 17 | 6 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2199 | 0 | 0 |
| 10 | iampedii/base64.txt | 167 | 59 | 53 | 51 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 645 | 238 | 157 |
| 12 | 0xRadikal/configs.txt | 1049 | 250 | 188 | 97 |
| 13 | configs_base64.txt | 4997 | 537 | 41 | 29 |
| 14 | F0rc3Run/proxies.txt | 68 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 1577 | 989 | 149 | 75 |
| 16 | ermaozi/v2ray.txt | 51 | 26 | 5 | 1 |
| 17 | ninjastrikers/all.txt | 2591 | 543 | 93 | 38 |
| 18 | Farid-Karimi/mixed_iran.txt | 533 | 247 | 59 | 15 |
| 19 | liketolivefree/sub.txt | 209 | 159 | 36 | 17 |
| 20 | roosterkid/V2RAY_BASE64.txt | 148 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 378 | 88 | 5 | 4 |
| 22 | barry-far/Sub4.txt | 500 | 115 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1565 | 708 | 50 | 31 |
| 24 | Mosifree/Reality | 266 | 160 | 0 | 0 |
| | **TOTAL** | **23513** | **8023** | **1411** | **761** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
