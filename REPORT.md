# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41422726756
- **Date (UTC):** 2026-11-02 09:53
- **Duration:** 6 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7754 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 7091 configs — **alive:** 1450 (1023 in allowed countries, 427 in other countries skipped)
- **Gemini-OK:** 782 of 1023 (241 Gemini-blocked)
- **Quality rejects:** 290 (jitter=200, dl=47, ka=32, up=11) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **610** configs = **610** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 123 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 224 |
| NL 🇳🇱 | 172 |
| DE 🇩🇪 | 77 |
| SG 🇸🇬 | 58 |
| FR 🇫🇷 | 34 |
| TR 🇹🇷 | 19 |
| GB 🇬🇧 | 17 |
| CH 🇨🇭 | 9 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 649 | 378 | 174 | 95 |
| 2 | miladtahanian/sub.txt | 106 | 40 | 2 | 0 |
| 3 | rtwo2/top.txt | 1000 | 669 | 255 | 127 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 62 | 19 | 9 |
| 5 | roosterkid/V2RAY_RAW.txt | 148 | 18 | 12 | 5 |
| 6 | MahanKenway/vless.txt | 138 | 26 | 11 | 9 |
| 7 | luckylukam/configs_tested.txt | 125 | 93 | 18 | 7 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2199 | 0 | 0 |
| 10 | iampedii/base64.txt | 167 | 59 | 55 | 55 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 645 | 224 | 148 |
| 12 | 0xRadikal/configs.txt | 1075 | 313 | 215 | 98 |
| 13 | configs_base64.txt | 4997 | 535 | 45 | 29 |
| 14 | F0rc3Run/proxies.txt | 68 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 924 | 485 | 173 | 87 |
| 16 | ermaozi/v2ray.txt | 51 | 28 | 6 | 1 |
| 17 | ninjastrikers/all.txt | 2591 | 580 | 97 | 40 |
| 18 | Farid-Karimi/mixed_iran.txt | 533 | 248 | 54 | 19 |
| 19 | liketolivefree/sub.txt | 209 | 159 | 34 | 20 |
| 20 | roosterkid/V2RAY_BASE64.txt | 148 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 378 | 88 | 5 | 4 |
| 22 | barry-far/Sub4.txt | 500 | 115 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1565 | 723 | 51 | 29 |
| 24 | Mosifree/Reality | 266 | 166 | 0 | 0 |
| | **TOTAL** | **22886** | **7641** | **1450** | **782** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
