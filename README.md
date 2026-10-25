# Github-Gemini — Gemini Sub Builder on GitHub Actions

[![Gemini Sub Builder (Github-Gemini)](https://github.com/pashadolf/Eternal-Sub/actions/workflows/gemini-builder.yml/badge.svg)](https://github.com/pashadolf/Eternal-Sub/actions/workflows/gemini-builder.yml)

تستر خودکار کانفیگ V2Ray روی GitHub Actions که هر روز یک ساب‌اسکریپشن آماده‌ی
Gemini می‌سازد. **کاملاً مستقل از فایل‌های قدیمی** (`gemini-sub.txt` و
`Eternal sub.txt`) کار می‌کند و فقط فایل‌های `Github-Gemini*.txt` و `REPORT.md`
را آپدیت می‌کند.

## لینک ساب

- **Raw:** `https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt`
- **jsDelivr (چند دقیقه دیرتر):** `https://cdn.jsdelivr.net/gh/pashadolf/Eternal-Sub@main/Github-Gemini.txt`
- گزارش آخرین اجرا: [`REPORT.md`](REPORT.md) — قیف کامل + جدول به‌تفکیک هر ساب

## ساختار

```
Eternal-Sub/
├── tester.py                    ← تستر (پایتون، بدون وابستگی خارجی)
├── settings.json                ← تنظیمات + لیست ساب‌های منبع (بدون توکن)
├── Github-Gemini.txt            ← خروجی: ساب base64 (تولید Actions)
├── Github-Gemini-plain.txt      ← خروجی: لیست خام برای دیباگ
├── REPORT.md                    ← گزارش آخرین اجرا
├── gemini-sub.txt               ← (قدیمی) خروجی اپ ویندوزی — دست‌نخورده
├── Eternal sub.txt              ← (قدیمی) فایل دستی — دست‌نخورده
└── .github/workflows/gemini-builder.yml
```

## چطور کار می‌کند

هر روز ساعت ~۹ صبح تهران (۰۵:۳۰ UTC؛ زمان‌بندی GitHub گاهی ۵–۲۰ دقیقه تأخیر
دارد) یا با اجرای دستی (Run workflow):

1. Xray-core آخرین نسخه دانلود می‌شود.
2. ۲۴ ساب منبع دانلود، دیکد و **dedup** می‌شوند (بر اساس سرور:پورت:UUID —
   نه اسم؛ برای vmess از JSON درون base64).
3. **دروازه‌ی فینگرپرینت:** کانفیگ بدون `fp` (شبیه‌سازی uTLS مرورگر) اصلاً
   تست نمی‌شود — فیلتر ضد DPI ایران. کانفیگ‌های Reality همیشه مجازند.
4. تست موازی (~۳۲ ورکر، هر ورکر پورت و xray مستقل خودش را دارد):
   - پینگ و لوکیشن با `cloudflare.com/cdn-cgi/trace` — فقط کشورهای مجاز ادامه می‌دهند
   - **چک عمیق Gemini:** کد HTTP نهایی باید ۲۰۰ باشد + بدنه‌ی کامل HTML +
     بدون پیام بلاک جغرافیایی
   - **باتری کیفیت** (برای ورود به ساب):
     - ۶ درخواست روی یک اتصال باز (keep-alive) + جیتر < ۸ برابر
     - دانلود کامل ۲.۵MB بدون استال (سرعت هرگز ۳ ثانیه زیر ۳۰KB/s نمی‌افتد)
     - آپلود ۵۱۲KB موفق
5. فقط کانفیگ‌های ♊Gemini وارد ساب می‌شوند (با rename: پرچم کشور + ♊Gemini؛
   US با پرچم 🇧🇿 اول لیست می‌آید) و با `GITHUB_TOKEN` خود Actions کامیٹ می‌شوند.
6. اگر هیچ کانفیگی پاس نشود، ساب قبلی دست‌نخورده می‌ماند (اجرای قرمز می‌شود).

## تنظیمات مهم (`settings.json`)

| کلید | مقدار فعلی | توضیح |
|---|---|---|
| `workers` | 32 | تعداد تست موازی |
| `allowed_countries` | US, DE, FR, NL, GB, CH, NO, TR, AE, SG | کشورهای مجاز |
| `require_fingerprint` | true | بدون fp تست نشود (ضد DPI؛ Reality مجاز) |
| `include_alive_no_gemini` | false | کانفیگ خوبِ بدون-Gemini هم وارد ساب شود؟ |
| `max_latency_ms` | 5000 | سقف پینگ |
| `dl_bytes` / `up_bytes` | 2.5MB / 512KB | حجم تست دانلود / آپلود |
| `ka_requests` / `ka_spread` | 6 / 8 | تعداد درخواست keep-alive / حداکثر جیتر |
| `max_configs` | 20000 | سقف تست هر اجرا |
| `runtime_budget_min` | 90 | سقف زمان تست (نگهبان امنیتی) |
| `subscription_urls` | ۲۴ آدرس | ساب‌های منبع |

## نکته‌ها

- ریپو باید **public** باشد تا لینک raw در کلاینت‌ها کار کند.
- هیچ توکنی در ریپو نیست؛ پوش با `GITHUB_TOKEN` خود Actions انجام می‌شود.
- تست‌ها از دیتاسنتر GitHub انجام می‌شوند؛ رفتار کانفیگ از اینترنت ایران می‌تواند
  متفاوت باشد — به همین دلیل فیلتر fp روش است.
