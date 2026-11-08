# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42471570019
- **Date (UTC):** 2026-11-08 10:32
- **Duration:** 4 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 7488 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5039 configs — **alive:** 276 (190 in allowed countries, 86 in other countries skipped)
- **Gemini-OK:** 83 of 190 (107 Gemini-blocked)
- **Quality rejects:** 58 (jitter=37, dl=11, ka=8, up=2) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **65** configs = **63** ♊Gemini + **2** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 69 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 17 |
| GB 🇬🇧 | 11 |
| SG 🇸🇬 | 11 |
| NL 🇳🇱 | 8 |
| DE 🇩🇪 | 8 |
| FI 🇫🇮 | 3 |
| FR 🇫🇷 | 2 |
| CA 🇨🇦 | 1 |
| SE 🇸🇪 | 1 |
| CH 🇨🇭 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 641 | 307 | 65 | 24 |
| 2 | R3ZARAHIMI/Original-Configs.txt | 157 | 62 | 7 | 3 |
| 3 | luckylukam/configs_tested.txt | 125 | 70 | 5 | 0 |
| 4 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 5 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 6 | configs_base64.txt | 5256 | 789 | 113 | 33 |
| 7 | ermaozi/v2ray.txt | 335 | 193 | 0 | 0 |
| 8 | ninjastrikers/all.txt | 2503 | 427 | 55 | 11 |
| 9 | Farid-Karimi/mixed_iran.txt | 582 | 125 | 11 | 4 |
| 10 | liketolivefree/sub.txt | 209 | 113 | 3 | 1 |
| 11 | roosterkid/V2RAY_BASE64.txt | 68 | 5 | 2 | 0 |
| 12 | MhdiTaheri/mix.txt | 384 | 74 | 0 | 0 |
| 13 | barry-far/Sub4.txt | 500 | 169 | 1 | 0 |
| 14 | 10ium/merged_base64 | 1680 | 679 | 14 | 7 |
| 15 | Mosifree/Reality | 266 | 123 | 0 | 0 |
| | **TOTAL** | **18358** | **5327** | **276** | **83** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
