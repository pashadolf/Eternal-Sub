# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42222754713
- **Date (UTC):** 2026-11-06 13:09
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7775 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5706 configs — **alive:** 353 (241 in allowed countries, 112 in other countries skipped)
- **Gemini-OK:** 124 of 241 (117 Gemini-blocked)
- **Quality rejects:** 83 (jitter=41, dl=25, ka=11, up=6) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **99** configs = **99** ♊Gemini + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 59 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 29 |
| DE 🇩🇪 | 20 |
| US 🇺🇸 | 16 |
| GB 🇬🇧 | 12 |
| TR 🇹🇷 | 12 |
| FR 🇫🇷 | 5 |
| CH 🇨🇭 | 2 |
| SG 🇸🇬 | 2 |
| NO 🇳🇴 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 666 | 329 | 61 | 18 |
| 2 | miladtahanian/sub.txt | 101 | 38 | 2 | 0 |
| 3 | rtwo2/top.txt | 999 | 545 | 49 | 12 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 167 | 60 | 8 | 3 |
| 5 | roosterkid/V2RAY_RAW.txt | 82 | 17 | 2 | 2 |
| 6 | MahanKenway/vless.txt | 129 | 8 | 0 | 0 |
| 7 | luckylukam/configs_tested.txt | 125 | 57 | 1 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2184 | 0 | 0 |
| 10 | iampedii/base64.txt | 103 | 18 | 4 | 2 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 253 | 41 | 11 |
| 12 | 0xRadikal/configs.txt | 956 | 209 | 127 | 48 |
| 13 | configs_base64.txt | 5051 | 442 | 3 | 2 |
| 14 | F0rc3Run/proxies.txt | 29 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 830 | 380 | 39 | 20 |
| 16 | ermaozi/v2ray.txt | 342 | 163 | 2 | 1 |
| 17 | ninjastrikers/all.txt | 2542 | 384 | 6 | 1 |
| 18 | Farid-Karimi/mixed_iran.txt | 554 | 104 | 2 | 1 |
| 19 | liketolivefree/sub.txt | 209 | 110 | 3 | 1 |
| 20 | roosterkid/V2RAY_BASE64.txt | 82 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 374 | 77 | 1 | 1 |
| 22 | barry-far/Sub4.txt | 500 | 134 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1588 | 554 | 2 | 1 |
| 24 | Mosifree/Reality | 266 | 123 | 0 | 0 |
| | **TOTAL** | **22793** | **6195** | **353** | **124** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
