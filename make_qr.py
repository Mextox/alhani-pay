"""يولّد QR للصفحة مع الشعار في المنتصف (تصحيح أخطاء عالٍ حتى يبقى قابلاً للمسح)."""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

URL = sys.argv[1] if len(sys.argv) > 1 else "http://169.58.143.252:8090"
qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=20, border=2)
qr.add_data(URL); qr.make(fit=True)
img = qr.make_image(fill_color="#1E1A17", back_color="white").convert("RGBA")
logo = Image.open("logo-orange.png").convert("RGBA")
size = img.width // 4
logo.thumbnail((size, size), Image.LANCZOS)
pad = 18
badge = Image.new("RGBA", (logo.width + pad*2, logo.height + pad*2), "white")
badge.paste(logo, (pad, pad), logo)
pos = ((img.width - badge.width)//2, (img.height - badge.height)//2)
img.paste(badge, pos, badge)
img.save("qr.png")
plain = qr.make_image(fill_color="#1E1A17", back_color="white"); plain.save("qr-plain.png")
print("qr.png", img.size, "→", URL)
