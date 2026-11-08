# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42477924667
- **Date (UTC):** 2026-11-08 12:00
- **Duration:** 4 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7795 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5839 configs — **alive:** 400 (289 in allowed countries, 111 in other countries skipped)
- **Gemini-OK:** 144 of 289 (145 Gemini-blocked)
- **Quality rejects:** 100 (jitter=62, ka=18, dl=13, up=7) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 2 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **104** configs = **101** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 86 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| GB 🇬🇧 | 35 |
| US 🇺🇸 | 20 |
| SG 🇸🇬 | 15 |
| NL 🇳🇱 | 10 |
| DE 🇩🇪 | 10 |
| FI 🇫🇮 | 5 |
| FR 🇫🇷 | 3 |
| CA 🇨🇦 | 1 |
| CH 🇨🇭 | 1 |
| SE 🇸🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 641 | 307 | 59 | 27 |
| 2 | miladtahanian/sub.txt | 62 | 19 | 3 | 1 |
| 3 | rtwo2/top.txt | 1000 | 496 | 53 | 10 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 149 | 55 | 11 | 5 |
| 5 | roosterkid/V2RAY_RAW.txt | 74 | 5 | 3 | 1 |
| 6 | MahanKenway/vless.txt | 130 | 9 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 60 | 3 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2183 | 0 | 0 |
| 10 | iampedii/base64.txt | 161 | 13 | 6 | 2 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 252 | 42 | 20 |
| 12 | 0xRadikal/configs.txt | 1073 | 300 | 141 | 46 |
| 13 | configs_base64.txt | 5240 | 500 | 20 | 11 |
| 14 | F0rc3Run/proxies.txt | 36 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 979 | 444 | 36 | 19 |
| 16 | ermaozi/v2ray.txt | 335 | 148 | 1 | 0 |
| 17 | ninjastrikers/all.txt | 2503 | 350 | 11 | 0 |
| 18 | Farid-Karimi/mixed_iran.txt | 582 | 113 | 4 | 1 |
| 19 | liketolivefree/sub.txt | 209 | 109 | 2 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 74 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 377 | 74 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 165 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1680 | 611 | 5 | 1 |
| 24 | Mosifree/Reality | 266 | 112 | 0 | 0 |
| | **TOTAL** | **23294** | **6331** | **400** | **144** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
