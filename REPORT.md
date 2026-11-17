# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/44102800304
- **Date (UTC):** 2026-11-17 14:27
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7815 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5480 configs — **alive:** 264 (194 in allowed countries, 70 in other countries skipped)
- **Gemini-OK:** 119 of 194 (75 Gemini-blocked)
- **Quality rejects:** 72 (jitter=39, dl=18, ka=13, up=2) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 4 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **87** configs = **84** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 34 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 22 |
| US 🇺🇸 | 16 |
| SG 🇸🇬 | 14 |
| GB 🇬🇧 | 13 |
| DE 🇩🇪 | 8 |
| FI 🇫🇮 | 3 |
| FR 🇫🇷 | 3 |
| TR 🇹🇷 | 3 |
| SE 🇸🇪 | 1 |
| AU 🇦🇺 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 218 | 117 | 18 | 8 |
| 2 | miladtahanian/sub.txt | 94 | 38 | 3 | 1 |
| 3 | rtwo2/top.txt | 1000 | 532 | 61 | 28 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 142 | 60 | 6 | 2 |
| 5 | roosterkid/V2RAY_RAW.txt | 81 | 19 | 7 | 6 |
| 6 | MahanKenway/vless.txt | 137 | 54 | 2 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 73 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 0 | 0 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 10 | iampedii/base64.txt | 117 | 14 | 3 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 403 | 28 | 17 |
| 12 | 0xRadikal/configs.txt | 868 | 158 | 74 | 34 |
| 13 | configs_base64.txt | 5578 | 479 | 6 | 1 |
| 14 | F0rc3Run/proxies.txt | 29 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 756 | 278 | 36 | 14 |
| 16 | ermaozi/v2ray.txt | 352 | 189 | 0 | 0 |
| 17 | ninjastrikers/all.txt | 2409 | 396 | 16 | 5 |
| 18 | Farid-Karimi/mixed_iran.txt | 515 | 115 | 0 | 0 |
| 19 | liketolivefree/sub.txt | 164 | 84 | 3 | 2 |
| 20 | roosterkid/V2RAY_BASE64.txt | 81 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 363 | 71 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 500 | 59 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1544 | 517 | 0 | 0 |
| 24 | Mosifree/Reality | 266 | 121 | 0 | 0 |
| | **TOTAL** | **22425** | **5962** | **264** | **119** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
