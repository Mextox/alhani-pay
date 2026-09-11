# الهاني مول — صفحة الحسابات المصرفية (QR)

صفحة واحدة ثابتة (`public/index.html`, مكتفية بذاتها، الشعار مضمّن) تعرض أرقام حسابات المول كنص قابل للنسخ بضغطة.

- **النشر:** `docker compose up -d` → nginx على المنفذ 8090 · الرابط الرسمي: https://mextox.github.io/alhani-pay/ (GitHub Pages) · نسخة احتياطية على السيرفر: http://169.58.143.252:8090
- **تعديل الأرقام:** عدّل مصفوفة `BANKS` داخل `public/index.html` (الاسم، رقم الحساب، IBAN اختياري) — لا حاجة لإعادة تشغيل الحاوية.
- **QR:** `.venv/bin/python make_qr.py "https://الرابط"` → `qr.png` (مع الشعار) و`qr-plain.png` (بدون). عند تغيير الرابط/الدومين أعد التوليد.
- الشعار: `logo-white.png` / `logo-orange.png` (خلفية شفافة) مستخرجان من شعار العميل.

---
## الحالة: مكتمل ومؤرشف (2026-09-11)

| العنصر | الرابط / المسار |
|---|---|
| الموقع (الإنتاج) | https://mextox.github.io/alhani-pay/ |
| نسخة السيرفر | http://169.58.143.252:8090 (حاوية `alhani-pay`) |
| لوحة التصاميم | https://claude.ai/code/artifact/ab25e3d5-2847-44aa-96c1-e17238eeb05a |
| ملف الطباعة | `الهاني مول — QR وتصاميم الطباعة.pdf` (5 صفحات، QR متجهي) |

**لاستئناف العمل:** عدّل `public/index.html` (مصفوفة `BANKS`) ثم:
```bash
git add -A && git commit -m "..." && git push origin main
git branch -D gh-pages; git subtree split --prefix public -b gh-pages && git push -f origin gh-pages
```
عند تغيير الرابط: `.venv/bin/python make_qr.py "https://..."` ثم `cd print && ../.venv/bin/python build_print.py` وأعد توليد الـ PDF.
