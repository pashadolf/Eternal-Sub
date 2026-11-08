# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42467459012
- **Date (UTC):** 2026-11-08 09:33
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 6806 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4453 configs — **alive:** 242 (164 in allowed countries, 78 in other countries skipped)
- **Gemini-OK:** 41 of 164 (123 Gemini-blocked)
- **Quality rejects:** 57 (jitter=35, dl=12, ka=10) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **35** configs = **32** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 75 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 11 |
| GB 🇬🇧 | 10 |
| DE 🇩🇪 | 6 |
| AU 🇦🇺 | 1 |
| CH 🇨🇭 | 1 |
| FI 🇫🇮 | 1 |
| NL 🇳🇱 | 1 |
| SG 🇸🇬 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 641 | 307 | 79 | 15 |
| 2 | luckylukam/configs_tested.txt | 125 | 71 | 7 | 0 |
| 3 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 4 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 5 | configs_base64.txt | 5240 | 776 | 114 | 18 |
| 6 | liketolivefree/sub.txt | 209 | 135 | 7 | 0 |
| 7 | roosterkid/V2RAY_BASE64.txt | 75 | 6 | 2 | 0 |
| 8 | MhdiTaheri/mix.txt | 384 | 91 | 4 | 0 |
| 9 | barry-far/Sub4.txt | 500 | 199 | 2 | 0 |
| 10 | 10ium/merged_base64 | 1680 | 731 | 27 | 8 |
| 11 | Mosifree/Reality | 266 | 131 | 0 | 0 |
| | **TOTAL** | **14772** | **4638** | **242** | **41** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
