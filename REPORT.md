# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/45211203651
- **Date (UTC):** 2026-11-23 16:01
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7978 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5447 configs — **alive:** 215 (158 in allowed countries, 57 in other countries skipped)
- **Gemini-OK:** 99 of 158 (59 Gemini-blocked)
- **Quality rejects:** 71 (jitter=34, dl=16, ka=14, up=7) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 3 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **60** configs = **60** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 24 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 16 |
| DE 🇩🇪 | 14 |
| SG 🇸🇬 | 11 |
| US 🇺🇸 | 8 |
| GB 🇬🇧 | 3 |
| FI 🇫🇮 | 2 |
| FR 🇫🇷 | 2 |
| AU 🇦🇺 | 1 |
| TR 🇹🇷 | 1 |
| CH 🇨🇭 | 1 |
| SE 🇸🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 192 | 77 | 16 | 9 |
| 2 | miladtahanian/sub.txt | 98 | 44 | 5 | 3 |
| 3 | rtwo2/top.txt | 1000 | 486 | 41 | 23 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 155 | 62 | 5 | 3 |
| 5 | roosterkid/V2RAY_RAW.txt | 73 | 15 | 5 | 2 |
| 6 | MahanKenway/vless.txt | 131 | 55 | 3 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 73 | 1 | 1 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 138 | 22 | 2 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 406 | 20 | 13 |
| 12 | 0xRadikal/configs.txt | 833 | 165 | 66 | 27 |
| 13 | configs_base64.txt | 5833 | 552 | 11 | 4 |
| 14 | F0rc3Run/proxies.txt | 97 | 7 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 780 | 253 | 24 | 6 |
| 16 | ermaozi/v2ray.txt | 241 | 106 | 1 | 1 |
| 17 | ninjastrikers/all.txt | 2353 | 337 | 11 | 3 |
| 18 | Farid-Karimi/mixed_iran.txt | 505 | 133 | 2 | 2 |
| 19 | liketolivefree/sub.txt | 156 | 78 | 0 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 73 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 353 | 79 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 177 | 8 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1634 | 622 | 1 | 0 |
| 24 | Mosifree/Reality | 266 | 121 | 0 | 0 |
| | **TOTAL** | **22299** | **5886** | **215** | **99** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
