# -*- coding: utf-8 -*-
"""يجمّع لوحات التصميم (.dc.html) في ملف طباعة واحد بأحجام صفحات مسماة، مع صفحة QR متجهي كبير."""
import re, base64
def body(name):
    s = open(f"{name}.dc.html", encoding="utf-8").read()
    return re.search(r'</helmet>\s*(.*?)\s*</x-dc>', s, re.S).group(1)
logo = base64.b64encode(open("logo.png","rb").read()).decode()
def inline_logo(h): return h.replace('src="logo.png"', f'src="data:image/png;base64,{logo}"')
main, poster, card, sticker = (inline_logo(body(n)) for n in ("Main","A4Poster","CounterCard","Sticker"))
big_qr = re.search(r'<svg.*?</svg>', poster, re.S).group(0).replace('width="380" height="380"', 'width="600" height="600"')
html = f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;800&display=swap">
<style>
@page {{ margin: 0; }}
@page a4 {{ size: 210mm 297mm; }} @page a5 {{ size: 148mm 210mm; }} @page a6l {{ size: 148mm 105mm; }} @page sq {{ size: 80mm 80mm; }}
body{{margin:0;font-family:'Tajawal','Segoe UI',Tahoma,Arial,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
section{{break-after:page;overflow:hidden;display:flex;align-items:center;justify-content:center;box-sizing:border-box}}
.a4{{page:a4;width:794px;height:1123px}} .a5{{page:a5;width:559px;height:794px}} .a6l{{page:a6l;width:559px;height:397px}} .sq{{page:sq;width:302px;height:302px}}
.frame{{display:flex;flex-direction:column;align-items:center;position:relative;overflow:hidden;box-sizing:border-box}}
</style></head><body>
<section class="a4"><div dir="rtl" class="frame" style="width:794px;height:1123px;background:#ffffff;justify-content:center;gap:34px;">
  <p style="margin:0;color:#1E1A17;font-size:34px;font-weight:800;">كود QR — الحسابات المصرفية للهاني مول</p>
  <div style="position:relative;width:600px;height:600px;">{big_qr}<div style="position:absolute;inset:0;display:grid;place-items:center"><div style="width:144px;height:144px;background:#fff;border-radius:24px;display:grid;place-items:center"><img src="data:image/png;base64,{logo}" style="width:102px;height:auto;display:block" alt=""></div></div></div>
  <p dir="ltr" style="margin:0;color:#FB6836;font-size:22px;font-weight:700;letter-spacing:.02em;">https://mextox.github.io/alhani-pay/</p>
  <p style="margin:0;color:#6F635D;font-size:15px;font-weight:500;">نسخة متجهية عالية الدقة — صالحة لأي مقاس طباعة</p>
</div></section>
<section class="a5"><div dir="rtl" class="frame" style="width:559px;height:794px;background:#FFF7F2;">{main}</div></section>
<section class="a4"><div dir="rtl" class="frame" style="width:794px;height:1123px;background:#FFF7F2;">{poster}</div></section>
<section class="a6l"><div dir="rtl" class="frame" style="width:559px;height:397px;background:#ffffff;">{card}</div></section>
<section class="sq" style="break-after:auto"><div dir="rtl" class="frame" style="width:302px;height:302px;background:#ffffff;">{sticker}</div></section>
</body></html>'''
open("../public/_print/print.html","w",encoding="utf-8").write(html); print("print.html written")
