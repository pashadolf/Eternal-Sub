# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/44543692915
- **Date (UTC):** 2026-11-19 14:29
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7859 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5384 configs — **alive:** 221 (174 in allowed countries, 47 in other countries skipped)
- **Gemini-OK:** 85 of 174 (89 Gemini-blocked)
- **Quality rejects:** 71 (jitter=41, dl=16, ka=14) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 3 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **51** configs = **51** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 49 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 14 |
| SG 🇸🇬 | 11 |
| NL 🇳🇱 | 9 |
| FI 🇫🇮 | 6 |
| DE 🇩🇪 | 5 |
| FR 🇫🇷 | 2 |
| AU 🇦🇺 | 2 |
| GB 🇬🇧 | 1 |
| SE 🇸🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 185 | 92 | 15 | 9 |
| 2 | miladtahanian/sub.txt | 110 | 32 | 2 | 1 |
| 3 | rtwo2/top.txt | 1000 | 530 | 61 | 20 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 163 | 69 | 7 | 2 |
| 5 | roosterkid/V2RAY_RAW.txt | 41 | 9 | 2 | 0 |
| 6 | MahanKenway/vless.txt | 111 | 44 | 1 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 73 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 103 | 8 | 5 | 3 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 410 | 23 | 15 |
| 12 | 0xRadikal/configs.txt | 796 | 155 | 55 | 23 |
| 13 | configs_base64.txt | 5589 | 502 | 13 | 3 |
| 14 | F0rc3Run/proxies.txt | 45 | 1 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 634 | 215 | 22 | 4 |
| 16 | ermaozi/v2ray.txt | 305 | 145 | 0 | 0 |
| 17 | ninjastrikers/all.txt | 2431 | 350 | 11 | 3 |
| 18 | Farid-Karimi/mixed_iran.txt | 576 | 143 | 1 | 0 |
| 19 | liketolivefree/sub.txt | 164 | 88 | 1 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 41 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 367 | 74 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 50 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1558 | 561 | 1 | 1 |
| 24 | Mosifree/Reality | 266 | 124 | 0 | 0 |
| | **TOTAL** | **22196** | **5860** | **221** | **85** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
