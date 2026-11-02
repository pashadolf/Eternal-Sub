# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41455370699
- **Date (UTC):** 2026-11-02 13:50
- **Duration:** 7 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7740 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 7178 configs — **alive:** 1423 (1003 in allowed countries, 420 in other countries skipped)
- **Gemini-OK:** 777 of 1003 (226 Gemini-blocked)
- **Quality rejects:** 217 (jitter=120, dl=51, ka=32, up=14) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **652** configs = **652** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 134 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 287 |
| NL 🇳🇱 | 156 |
| DE 🇩🇪 | 60 |
| FR 🇫🇷 | 53 |
| SG 🇸🇬 | 49 |
| TR 🇹🇷 | 20 |
| GB 🇬🇧 | 16 |
| CH 🇨🇭 | 11 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 649 | 378 | 172 | 86 |
| 2 | miladtahanian/sub.txt | 106 | 40 | 1 | 1 |
| 3 | rtwo2/top.txt | 1000 | 669 | 222 | 123 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 141 | 57 | 26 | 19 |
| 5 | roosterkid/V2RAY_RAW.txt | 147 | 42 | 22 | 8 |
| 6 | MahanKenway/vless.txt | 138 | 25 | 13 | 10 |
| 7 | luckylukam/configs_tested.txt | 125 | 93 | 18 | 7 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2199 | 0 | 0 |
| 10 | iampedii/base64.txt | 157 | 84 | 70 | 60 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 645 | 250 | 160 |
| 12 | 0xRadikal/configs.txt | 1026 | 278 | 173 | 85 |
| 13 | configs_base64.txt | 4997 | 569 | 52 | 30 |
| 14 | F0rc3Run/proxies.txt | 68 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 924 | 512 | 171 | 83 |
| 16 | ermaozi/v2ray.txt | 32 | 20 | 7 | 1 |
| 17 | ninjastrikers/all.txt | 2591 | 588 | 104 | 40 |
| 18 | Farid-Karimi/mixed_iran.txt | 533 | 239 | 48 | 15 |
| 19 | liketolivefree/sub.txt | 209 | 159 | 27 | 18 |
| 20 | roosterkid/V2RAY_BASE64.txt | 147 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 378 | 88 | 4 | 3 |
| 22 | barry-far/Sub4.txt | 500 | 141 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1565 | 723 | 43 | 28 |
| 24 | Mosifree/Reality | 266 | 166 | 0 | 0 |
| | **TOTAL** | **22797** | **7727** | **1423** | **777** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
