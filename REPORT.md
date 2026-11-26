# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/45847488328
- **Date (UTC):** 2026-11-26 15:19
- **Duration:** 2 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7550 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4644 configs — **alive:** 130 (98 in allowed countries, 32 in other countries skipped)
- **Gemini-OK:** 70 of 98 (28 Gemini-blocked)
- **Quality rejects:** 32 (jitter=20, dl=5, ka=5, up=2) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 7 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **41** configs = **41** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 18 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| SG 🇸🇬 | 12 |
| NL 🇳🇱 | 11 |
| US 🇺🇸 | 7 |
| DE 🇩🇪 | 5 |
| FI 🇫🇮 | 2 |
| CA 🇨🇦 | 1 |
| FR 🇫🇷 | 1 |
| AU 🇦🇺 | 1 |
| CH 🇨🇭 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 126 | 56 | 10 | 6 |
| 2 | miladtahanian/sub.txt | 189 | 134 | 7 | 2 |
| 3 | R3ZARAHIMI/Original-Configs.txt | 148 | 56 | 9 | 6 |
| 4 | roosterkid/V2RAY_RAW.txt | 51 | 7 | 1 | 0 |
| 5 | MahanKenway/vless.txt | 125 | 54 | 1 | 0 |
| 6 | luckylukam/configs_tested.txt | 125 | 76 | 1 | 1 |
| 7 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 8 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 9 | iampedii/base64.txt | 58 | 3 | 2 | 2 |
| 10 | Au1rxx/v2ray-base64.txt | 1446 | 430 | 30 | 22 |
| 11 | 0xRadikal/configs.txt | 627 | 119 | 39 | 23 |
| 12 | configs_base64.txt | 5626 | 514 | 13 | 1 |
| 13 | F0rc3Run/proxies.txt | 90 | 5 | 0 | 0 |
| 14 | ermaozi/v2ray.txt | 211 | 85 | 3 | 1 |
| 15 | ninjastrikers/all.txt | 2331 | 341 | 8 | 4 |
| 16 | Farid-Karimi/mixed_iran.txt | 442 | 96 | 0 | 0 |
| 17 | liketolivefree/sub.txt | 156 | 85 | 1 | 1 |
| 18 | roosterkid/V2RAY_BASE64.txt | 51 | 0 | 0 | 0 |
| 19 | MhdiTaheri/mix.txt | 364 | 72 | 0 | 0 |
| 20 | barry-far/Sub4.txt | 354 | 12 | 0 | 0 |
| 21 | 10ium/merged_base64 | 1548 | 634 | 5 | 1 |
| 22 | Mosifree/Reality | 209 | 37 | 0 | 0 |
| | **TOTAL** | **19917** | **5001** | **130** | **70** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
