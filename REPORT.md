# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41048525453
- **Date (UTC):** 2026-10-30 11:38
- **Duration:** 8 min
- **Xray core:** v26.10.29

## Funnel

- **No-fingerprint excluded:** 5233 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5866 configs — **alive:** 1672 (1193 in allowed countries, 479 in other countries skipped)
- **Gemini-OK:** 902 of 1193 (291 Gemini-blocked)
- **Quality rejects:** 222 (jitter=101, dl=69, ka=42, up=10) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **797** configs = **797** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 174 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 400 |
| NL 🇳🇱 | 182 |
| FR 🇫🇷 | 76 |
| DE 🇩🇪 | 60 |
| SG 🇸🇬 | 38 |
| GB 🇬🇧 | 21 |
| CH 🇨🇭 | 10 |
| TR 🇹🇷 | 10 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 657 | 355 | 161 | 84 |
| 2 | miladtahanian/sub.txt | 200 | 72 | 6 | 5 |
| 3 | rtwo2/top.txt | 1000 | 649 | 235 | 124 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 161 | 70 | 18 | 9 |
| 5 | roosterkid/V2RAY_RAW.txt | 130 | 27 | 10 | 4 |
| 6 | MahanKenway/vless.txt | 139 | 20 | 6 | 1 |
| 7 | luckylukam/configs_tested.txt | 125 | 94 | 23 | 6 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 26 | 26 | 0 | 0 |
| 10 | iampedii/base64.txt | 203 | 60 | 48 | 41 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 652 | 544 | 320 |
| 12 | 0xRadikal/configs.txt | 1190 | 288 | 140 | 66 |
| 13 | configs_base64.txt | 4758 | 622 | 101 | 50 |
| 14 | F0rc3Run/proxies.txt | 55 | 1 | 1 | 1 |
| 15 | Delta-Kronecker/vless.txt | 820 | 440 | 153 | 81 |
| 16 | ermaozi/v2ray.txt | 398 | 167 | 7 | 5 |
| 17 | ninjastrikers/all.txt | 2554 | 606 | 96 | 44 |
| 18 | Farid-Karimi/mixed_iran.txt | 560 | 234 | 48 | 18 |
| 19 | liketolivefree/sub.txt | 425 | 303 | 22 | 5 |
| 20 | roosterkid/V2RAY_BASE64.txt | 130 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 389 | 79 | 3 | 2 |
| 22 | barry-far/Sub4.txt | 500 | 209 | 7 | 3 |
| 23 | 10ium/merged_base64 | 1454 | 715 | 43 | 33 |
| 24 | Mosifree/Reality | 266 | 165 | 0 | 0 |
| | **TOTAL** | **17598** | **5866** | **1672** | **902** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
