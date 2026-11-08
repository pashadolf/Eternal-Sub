# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42474233086
- **Date (UTC):** 2026-11-08 11:10
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7796 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5826 configs — **alive:** 393 (282 in allowed countries, 111 in other countries skipped)
- **Gemini-OK:** 138 of 282 (144 Gemini-blocked)
- **Quality rejects:** 91 (jitter=53, dl=20, ka=13, up=5) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 2 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **101** configs = **98** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 91 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| GB 🇬🇧 | 32 |
| US 🇺🇸 | 20 |
| SG 🇸🇬 | 15 |
| DE 🇩🇪 | 13 |
| NL 🇳🇱 | 6 |
| FR 🇫🇷 | 4 |
| FI 🇫🇮 | 3 |
| CA 🇨🇦 | 2 |
| CH 🇨🇭 | 1 |
| AU 🇦🇺 | 1 |
| SE 🇸🇪 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 641 | 307 | 59 | 28 |
| 2 | miladtahanian/sub.txt | 79 | 13 | 1 | 1 |
| 3 | rtwo2/top.txt | 1000 | 497 | 61 | 12 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 157 | 59 | 6 | 1 |
| 5 | roosterkid/V2RAY_RAW.txt | 74 | 5 | 3 | 1 |
| 6 | MahanKenway/vless.txt | 130 | 7 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 60 | 2 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2183 | 0 | 0 |
| 10 | iampedii/base64.txt | 161 | 13 | 6 | 2 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 252 | 42 | 18 |
| 12 | 0xRadikal/configs.txt | 1037 | 290 | 144 | 43 |
| 13 | configs_base64.txt | 5240 | 509 | 18 | 10 |
| 14 | F0rc3Run/proxies.txt | 36 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 979 | 440 | 35 | 20 |
| 16 | ermaozi/v2ray.txt | 335 | 149 | 1 | 0 |
| 17 | ninjastrikers/all.txt | 2503 | 351 | 9 | 1 |
| 18 | Farid-Karimi/mixed_iran.txt | 582 | 108 | 2 | 1 |
| 19 | liketolivefree/sub.txt | 209 | 109 | 2 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 74 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 384 | 74 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 163 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1680 | 611 | 2 | 0 |
| 24 | Mosifree/Reality | 266 | 112 | 0 | 0 |
| | **TOTAL** | **23290** | **6318** | **393** | **138** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
