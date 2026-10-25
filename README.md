# Github-Gemini — Gemini Sub Builder on GitHub Actions

این ریپو یه تستر خودکار کانفیگ V2Ray است که روی GitHub Actions اجرا می‌شه و یه
ساب‌اسکریپشن آماده‌ی Gemini می‌سازه. **کاملاً مستقل از فایل `gemini-sub.txt`**
کار می‌کند (آن فایل مال اسکریپت ویندوزی محلی است و این workflow به آن دست نمی‌زند).

## ساختار فایل‌ها در ریپو

```
Eternal-Sub/
├── tester.py                          ← تستر کراس‌پلتفرم
├── settings.json                      ← تنظیمات + لیست ساب‌ها (بدون توکن)
├── Github-Gemini.txt                  ← خروجی: ساب base64 (ساخته‌شده توسط Actions)
├── Github-Gemini-plain.txt            ← خروجی: لیست خام برای دیباگ
├── REPORT.md                          ← گزارش آخرین اجرا (جدول به‌تفکیک هر ساب)
└── .github/workflows/gemini-builder.yml
```

## لینک ساب (بعد از اولین اجرا)

- **Raw:** `https://raw.githubusercontent.com/pashadolf/Eternal-Sub/main/Github-Gemini.txt`
- **jsDelivr:** `https://cdn.jsdelivr.net/gh/pashadolf/Eternal-Sub@main/Github-Gemini.txt`

## چطور کار می‌کند

1. هر روز ساعت ۹ صبح به وقت تهران (۰۵:۳۰ UTC) یا با اجرای دستی (workflow_dispatch) اجرا می‌شود.
2. Xray-core آخرین نسخه دانلود می‌شود.
3. `tester.py` ساب‌ها را دانلود، تکراری‌ها را حذف، و همه را موازی تست می‌کند:
   - پینگ و لوکیشن با `cloudflare.com/cdn-cgi/trace`
   - چک عمیق Gemini (طول HTML + متن‌های بلاک کشور) فقط برای کشورهای مجاز
4. کانفیگ‌های پاس‌شده rename می‌شوند (پرچم + ♊Gemini؛ US با پرچم 🇧🇿 اول لیست می‌آید)
   و در `Github-Gemini.txt` (base64) commit می‌شوند.
5. اگر هیچ کانفیگی پاس نکند، فایل قبلی دست‌نخورده می‌ماند (job قرمز می‌شود).

## اجرای دستی

تب **Actions** → **Gemini Sub Builder** → **Run workflow**.

یا لوکال (ویندوز):

```
python tester.py --configs-file configs.txt --workers 10 --out-prefix local-test
```

(اگر xray کنار Happ نصب باشد خودش پیدایش می‌کند؛ وگرنه `--xray PATH` بده.)

## تنظیمات مهم (`settings.json`)

| کلید | پیش‌فرض | توضیح |
|---|---|---|
| `workers` | 32 | تعداد تست موازی |
| `max_configs` | 6000 | سقف تعداد کانفیگ تست‌شده در هر اجرا |
| `runtime_budget_min` | 90 | بعد از این دقیقه، تست جدید شروع نمی‌شود |
| `max_latency_ms` | 5000 | سقف پینگ |
| `allowed_countries` | US, DE, NL, ... | کشورهای مجاز برای ورود به ساب |
| `include_alive_no_gemini` | true | کانفیگ زنده‌ی بدون-Gemini از کشور مجاز هم وارد ساب شود |
| `subscription_urls` | — | لیست ساب‌های منبع |

## نکته‌ها

- زمان‌بندی GitHub گاهی ۵ تا ۲۰ دقیقه تأخیر دارد؛ یعنی اجرا معمولاً بین ۱۰:۰۰ تا ۱۰:۲۰ صبح شروع می‌شود.
- ریپو باید **public** باشد تا لینک raw داخل کلاینت‌ها کار کند.
- نیازی به هیچ توکنی نیست؛ از `GITHUB_TOKEN` خود Actions استفاده می‌شود.
- تداخلی با `gemini-sub.txt` نیست: این workflow فقط `Github-Gemini*.txt` را commit می‌کند.
