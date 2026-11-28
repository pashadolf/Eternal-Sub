# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/46153503616
- **Date (UTC):** 2026-11-28 14:15
- **Duration:** 2 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7613 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4699 configs — **alive:** 143 (105 in allowed countries, 38 in other countries skipped)
- **Gemini-OK:** 74 of 105 (31 Gemini-blocked)
- **Quality rejects:** 37 (jitter=21, ka=10, dl=6) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 3 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **52** configs = **52** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 13 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 21 |
| DE 🇩🇪 | 10 |
| SG 🇸🇬 | 8 |
| US 🇺🇸 | 7 |
| FR 🇫🇷 | 2 |
| FI 🇫🇮 | 2 |
| CA 🇨🇦 | 1 |
| AU 🇦🇺 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 151 | 73 | 19 | 14 |
| 2 | miladtahanian/sub.txt | 193 | 122 | 1 | 1 |
| 3 | R3ZARAHIMI/Original-Configs.txt | 134 | 63 | 7 | 4 |
| 4 | roosterkid/V2RAY_RAW.txt | 38 | 8 | 0 | 0 |
| 5 | MahanKenway/vless.txt | 135 | 65 | 4 | 2 |
| 6 | luckylukam/configs_tested.txt | 125 | 77 | 1 | 1 |
| 7 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 8 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 9 | iampedii/base64.txt | 104 | 38 | 3 | 2 |
| 10 | Au1rxx/v2ray-base64.txt | 1446 | 426 | 23 | 15 |
| 11 | 0xRadikal/configs.txt | 577 | 133 | 41 | 21 |
| 12 | configs_base64.txt | 5607 | 536 | 16 | 5 |
| 13 | F0rc3Run/proxies.txt | 96 | 2 | 0 | 0 |
| 14 | ermaozi/v2ray.txt | 219 | 106 | 2 | 1 |
| 15 | ninjastrikers/all.txt | 2300 | 394 | 14 | 2 |
| 16 | Farid-Karimi/mixed_iran.txt | 298 | 70 | 4 | 1 |
| 17 | liketolivefree/sub.txt | 156 | 84 | 0 | 0 |
| 18 | roosterkid/V2RAY_BASE64.txt | 38 | 0 | 0 | 0 |
| 19 | MhdiTaheri/mix.txt | 345 | 71 | 0 | 0 |
| 20 | barry-far/Sub4.txt | 174 | 11 | 0 | 0 |
| 21 | 10ium/merged_base64 | 1542 | 545 | 8 | 5 |
| 22 | Mosifree/Reality | 209 | 42 | 0 | 0 |
| | **TOTAL** | **19527** | **5051** | **143** | **74** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
