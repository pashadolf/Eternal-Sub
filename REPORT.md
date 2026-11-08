# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42470990084
- **Date (UTC):** 2026-11-08 10:23
- **Duration:** 3 min
- **Xray core:** v26.10.31

## Funnel

- **No-fingerprint excluded:** 6815 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 4471 configs — **alive:** 223 (153 in allowed countries, 70 in other countries skipped)
- **Gemini-OK:** 63 of 153 (90 Gemini-blocked)
- **Quality rejects:** 54 (jitter=37, dl=10, ka=5, up=2) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **In sub:** **50** configs = **47** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 52 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| US 🇺🇸 | 15 |
| SG 🇸🇬 | 10 |
| DE 🇩🇪 | 9 |
| GB 🇬🇧 | 5 |
| CA 🇨🇦 | 3 |
| NL 🇳🇱 | 3 |
| FR 🇫🇷 | 1 |
| CH 🇨🇭 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 641 | 307 | 77 | 28 |
| 2 | luckylukam/configs_tested.txt | 125 | 71 | 6 | 0 |
| 3 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 4 | teknovpnhub/test2 | 5640 | 2185 | 0 | 0 |
| 5 | configs_base64.txt | 5256 | 798 | 106 | 22 |
| 6 | liketolivefree/sub.txt | 209 | 134 | 6 | 1 |
| 7 | roosterkid/V2RAY_BASE64.txt | 68 | 5 | 1 | 0 |
| 8 | MhdiTaheri/mix.txt | 384 | 91 | 3 | 1 |
| 9 | barry-far/Sub4.txt | 500 | 200 | 1 | 0 |
| 10 | 10ium/merged_base64 | 1680 | 731 | 23 | 11 |
| 11 | Mosifree/Reality | 266 | 131 | 0 | 0 |
| | **TOTAL** | **14781** | **4659** | **223** | **63** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
