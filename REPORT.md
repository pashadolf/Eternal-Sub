# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/45647101614
- **Date (UTC):** 2026-11-25 15:39
- **Duration:** 2 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7729 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5256 configs — **alive:** 153 (108 in allowed countries, 45 in other countries skipped)
- **Gemini-OK:** 74 of 108 (34 Gemini-blocked)
- **Quality rejects:** 46 (jitter=21, ka=16, dl=9) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 13 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **35** configs = **35** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 14 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| SG 🇸🇬 | 14 |
| DE 🇩🇪 | 8 |
| NL 🇳🇱 | 5 |
| US 🇺🇸 | 3 |
| FI 🇫🇮 | 3 |
| SE 🇸🇪 | 1 |
| CH 🇨🇭 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 169 | 72 | 13 | 6 |
| 2 | miladtahanian/sub.txt | 159 | 110 | 3 | 0 |
| 3 | rtwo2/top.txt | 1000 | 571 | 38 | 18 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 131 | 50 | 5 | 3 |
| 5 | roosterkid/V2RAY_RAW.txt | 35 | 12 | 1 | 0 |
| 6 | MahanKenway/vless.txt | 121 | 52 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 73 | 0 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 67 | 13 | 2 | 0 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 424 | 29 | 21 |
| 12 | 0xRadikal/configs.txt | 611 | 128 | 29 | 17 |
| 13 | configs_base64.txt | 5785 | 565 | 16 | 4 |
| 14 | F0rc3Run/proxies.txt | 107 | 3 | 0 | 0 |
| 15 | ermaozi/v2ray.txt | 220 | 104 | 1 | 0 |
| 16 | ninjastrikers/all.txt | 2435 | 391 | 11 | 3 |
| 17 | Farid-Karimi/mixed_iran.txt | 163 | 71 | 0 | 0 |
| 18 | liketolivefree/sub.txt | 156 | 78 | 1 | 0 |
| 19 | roosterkid/V2RAY_BASE64.txt | 35 | 0 | 0 | 0 |
| 20 | MhdiTaheri/mix.txt | 346 | 70 | 0 | 0 |
| 21 | barry-far/Sub4.txt | 500 | 70 | 0 | 0 |
| 22 | 10ium/merged_base64 | 1493 | 562 | 4 | 2 |
| 23 | Mosifree/Reality | 209 | 43 | 0 | 0 |
| | **TOTAL** | **20953** | **5647** | **153** | **74** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
