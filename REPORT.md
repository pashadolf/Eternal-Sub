# Github-Gemini — Build Report

- **Run:** https://github.com/pashadolf/Eternal-Sub/actions/runs/42629584769
- **Date (UTC):** 2026-11-09 13:58
- **Duration:** 3 min
- **Xray core:** v26.11.9

## Funnel

- **No-fingerprint excluded:** 7794 configs (require_fingerprint=true — no uTLS fp in link)
- **Tested:** 5771 configs — **alive:** 397 (298 in allowed countries, 99 in other countries skipped)
- **Gemini-OK:** 146 of 298 (152 Gemini-blocked)
- **Quality rejects:** 118 (jitter=75, dl=23, ka=12, up=8) — ka=keep-alive, jitter, dl=download/speed, up=upload
- **GreyNoise excluded:** 2 configs (super-noisy / suspicious / malicious scanner IPs filtered out)
- **In sub:** **90** configs = **87** ♊Gemini + **3** Iran (🇮🇷 domestic/tunnel) + **0** alive-only (allowed country, no Gemini, passed quality)
- **Excluded alive-only:** 91 configs passed quality but are NOT in the sub (include_alive_no_gemini=false)

## ♊Gemini configs in sub by country

| Country | Gemini-OK |
|---|---|
| NL 🇳🇱 | 21 |
| US 🇺🇸 | 18 |
| DE 🇩🇪 | 14 |
| SG 🇸🇬 | 14 |
| GB 🇬🇧 | 11 |
| SE 🇸🇪 | 4 |
| TR 🇹🇷 | 3 |
| FI 🇫🇮 | 1 |
| NO 🇳🇴 | 1 |

## Per-subscription performance

| # | Subscription | Fetched | Unique | Alive | Gemini OK |
|---|---|---|---|---|---|
| 1 | pourih/verified.txt | 652 | 312 | 57 | 29 |
| 2 | miladtahanian/sub.txt | 125 | 52 | 3 | 0 |
| 3 | rtwo2/top.txt | 1000 | 474 | 78 | 19 |
| 4 | R3ZARAHIMI/Original-Configs.txt | 164 | 68 | 8 | 7 |
| 5 | roosterkid/V2RAY_RAW.txt | 69 | 10 | 2 | 1 |
| 6 | MahanKenway/vless.txt | 132 | 10 | 1 | 1 |
| 7 | luckylukam/configs_tested.txt | 125 | 59 | 2 | 0 |
| 8 | ThomasJasperthecat/sublist1.txt | 12 | 6 | 0 | 0 |
| 9 | teknovpnhub/test2 | 5640 | 2184 | 0 | 0 |
| 10 | iampedii/base64.txt | 108 | 12 | 2 | 1 |
| 11 | Au1rxx/v2ray-base64.txt | 1446 | 248 | 35 | 13 |
| 12 | 0xRadikal/configs.txt | 1120 | 284 | 145 | 39 |
| 13 | configs_base64.txt | 5252 | 470 | 10 | 3 |
| 14 | F0rc3Run/proxies.txt | 43 | 0 | 0 | 0 |
| 15 | Delta-Kronecker/vless.txt | 823 | 316 | 41 | 29 |
| 16 | ermaozi/v2ray.txt | 344 | 186 | 1 | 0 |
| 17 | ninjastrikers/all.txt | 2505 | 375 | 6 | 2 |
| 18 | Farid-Karimi/mixed_iran.txt | 586 | 127 | 3 | 1 |
| 19 | liketolivefree/sub.txt | 209 | 112 | 2 | 0 |
| 20 | roosterkid/V2RAY_BASE64.txt | 69 | 0 | 0 | 0 |
| 21 | MhdiTaheri/mix.txt | 388 | 74 | 0 | 0 |
| 22 | barry-far/Sub4.txt | 496 | 159 | 0 | 0 |
| 23 | 10ium/merged_base64 | 1597 | 566 | 1 | 1 |
| 24 | Mosifree/Reality | 266 | 115 | 0 | 0 |
| | **TOTAL** | **23171** | **6219** | **397** | **146** |

**Subscription:** https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt
