# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/41309922007
- **Date (UTC):** 2026-11-01 13:17
- **Duration:** 7 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 8105 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 7622 configs — **alive:** 1538 (1104 in allowed countries, 434 in other countries skipped)
- **Gemini-OK:** 726 of 1104 (378 Gemini-blocked)
- **Quality rejects:** 251 (jitter=157, dl=53, ka=30, up=11) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **608** configs = **608** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 245 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 272 |
| NL 🇳🇱 | 129 |
| DE 🇩🇪 | 67 |
| SG 🇸🇬 | 51 |
| FR 🇫🇷 | 44 |
| TR 🇹🇷 | 15 |
| GB 🇬🇧 | 14 |
| CH 🇨🇭 | 14 |
| AE 🇦🇪 | 2 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 614 | 340 | 151 | 85 |
| 2 | miladtahanian/sub.txt | 243 | 120 | 3 | 1 |
| 3 | rtwo2/top.txt | 1000 | 659 | 255 | 112 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 150 | 61 | 22 | 15 |
| 5 | roosterkid/V2RAY_RAW.txt | 143 | 15 | 4 | 1 |
| 6 | MahanKenway/vless.txt | 140 | 19 | 8 | 7 |
| 7 | luckylukam/configs_tested.txt | 125 | 95 | 18 | 7 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 12 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2199 | 0 | 0 |
| 10 | iampedii/base64.txt | 111 | 30 | 25 | 23 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 637 | 257 | 161 |
| 12 | 0xRadikal/configs.txt | 1821 | 673 | 345 | 115 |
| 13 | configs_base64.txt | 5133 | 462 | 23 | 8 |
| 14 | F0rc3Run/proxies.txt | 48 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 1577 | 738 | 156 | 62 |
| 16 | ermaozi/v2ray.txt | 66 | 27 | 2 | 1 |
| 17 | ninjastrikers/all.txt | 2604 | 602 | 116 | 44 |
| 18 | Farid-Karimi/mixed_iran.txt | 584 | 262 | 58 | 23 |
| 19 | liketolivefree/sub.txt | 209 | 150 | 41 | 23 |
| 20 | roosterkid/V2RAY_BASE64.txt | 143 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 373 | 83 | 2 | 2 |
| 22 | barry-far/Sub4.txt | 500 | 163 | 3 | 3 |
| 23 | 10ium/merged_base64 | 1535 | 696 | 49 | 33 |
| 24 | Mosifree/Reality | 266 | 160 | 0 | 0 |
| | **TOTAL** | **24483** | **8203** | **1538** | **726** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
