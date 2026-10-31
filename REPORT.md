# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41195027582
- **Date (UTC):** 2026-10-31 11:08
- **Duration:** 7 min
- **Xray core:** v26.10.29

## Funnel

- **No-fingerprint excluded:** 5263 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5660 configs — **alive:** 1765 (1221 in allowed countries, 544 in other countries skipped)
- **Gemini-OK:** 895 of 1221 (326 Gemini-blocked)
- **Quality rejects:** 274 (jitter=131, dl=110, ka=27, up=6) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **746** configs = **746** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 201 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 404 |
| NL 🇳🇱 | 142 |
| DE 🇩🇪 | 57 |
| FR 🇫🇷 | 55 |
| SG 🇸🇬 | 46 |
| CH 🇨🇭 | 20 |
| GB 🇬🇧 | 12 |
| TR 🇹🇷 | 10 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 677 | 400 | 189 | 87 |
| 2 | miladtahanian/sub.txt | 221 | 132 | 32 | 26 |
| 3 | rtwo2/top.txt | 1000 | 617 | 226 | 110 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 162 | 71 | 25 | 8 |
| 5 | roosterkid/V2RAY_RAW.txt | 145 | 56 | 36 | 16 |
| 6 | MahanKenway/vless.txt | 151 | 20 | 9 | 5 |
| 7 | luckylukam/configs_tested.txt | 125 | 94 | 26 | 8 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 194 | 73 | 49 | 43 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 644 | 541 | 296 |
| 12 | 0xRadikal/configs.txt | 1289 | 309 | 149 | 69 |
| 13 | configs_base64.txt | 4899 | 470 | 26 | 3 |
| 14 | F0rc3Run/proxies.txt | 72 | 1 | 1 | 1 |
| 15 | Delta-Kronecker/vless.txt | 826 | 449 | 141 | 74 |
| 16 | ermaozi/v2ray.txt | 417 | 173 | 2 | 1 |
| 17 | ninjastrikers/all.txt | 2561 | 566 | 122 | 44 |
| 18 | Farid-Karimi/mixed_iran.txt | 580 | 258 | 55 | 17 |
| 19 | liketolivefree/sub.txt | 209 | 149 | 72 | 46 |
| 20 | roosterkid/V2RAY_BASE64.txt | 145 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 392 | 87 | 3 | 2 |
| 22 | barry-far/Sub4.txt | 500 | 170 | 6 | 4 |
| 23 | 10ium/merged_base64 | 1453 | 721 | 55 | 35 |
| 24 | Mosifree/Reality | 266 | 162 | 0 | 0 |
| | **TOTAL** | **17768** | **5660** | **1765** | **895** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
