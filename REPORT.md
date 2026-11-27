# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/46021762725
- **Date (UTC):** 2026-11-27 15:08
- **Duration:** 2 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7623 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4664 configs — **alive:** 143 (116 in allowed countries, 27 in other countries skipped)
- **Gemini-OK:** 54 of 116 (62 Gemini-blocked)
- **Quality rejects:** 30 (jitter=16, ka=7, dl=4, up=3) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 5 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **39** configs = **39** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 42 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 12 |
| NL 🇳🇱 | 10 |
| SG 🇸🇬 | 9 |
| DE 🇩🇪 | 3 |
| FI 🇫🇮 | 2 |
| CA 🇨🇦 | 1 |
| FR 🇫🇷 | 1 |
| AU 🇦🇺 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 148 | 69 | 13 | 9 |
| 2 | miladtahanian/sub.txt | 182 | 126 | 0 | 0 |
| 3 | R3ZARAHIMI/Original-Configs.txt | 137 | 66 | 7 | 2 |
| 4 | roosterkid/V2RAY_RAW.txt | 26 | 3 | 0 | 0 |
| 5 | MahanKenway/vless.txt | 130 | 59 | 1 | 0 |
| 6 | luckylukam/configs_tested.txt | 125 | 77 | 1 | 0 |
| 7 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 8 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 9 | iampedii/base64.txt | 78 | 9 | 3 | 2 |
| 10 | Au1rxx/v2ray-base64.txt | 1446 | 427 | 17 | 10 |
| 11 | 0xRadikal/configs.txt | 472 | 98 | 36 | 21 |
| 12 | configs_base64.txt | 5699 | 512 | 15 | 2 |
| 13 | F0rc3Run/proxies.txt | 97 | 8 | 0 | 0 |
| 14 | ermaozi/v2ray.txt | 236 | 117 | 0 | 0 |
| 15 | ninjastrikers/all.txt | 2358 | 364 | 12 | 5 |
| 16 | Farid-Karimi/mixed_iran.txt | 342 | 82 | 3 | 1 |
| 17 | liketolivefree/sub.txt | 156 | 82 | 1 | 1 |
| 18 | roosterkid/V2RAY_BASE64.txt | 26 | 0 | 0 | 0 |
| 19 | MhdiTaheri/mix.txt | 342 | 70 | 0 | 0 |
| 20 | barry-far/Sub4.txt | 287 | 4 | 0 | 0 |
| 21 | 10ium/merged_base64 | 1515 | 586 | 34 | 1 |
| 22 | Mosifree/Reality | 209 | 42 | 0 | 0 |
| | **TOTAL** | **19651** | **4986** | **143** | **54** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
