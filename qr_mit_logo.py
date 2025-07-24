from PIL import Image, ImageEnhance
import qrcode

# === Pfade ===
logo_path = "logoSG.png"
output_path = "qr_mit_logo.png"
url = "https://sugu4.github.io/guemues/"

# === QR-Code ===
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# === Logo vorbereiten ===
logo = Image.open(logo_path).convert("RGBA")
logo = logo.resize((66, 66), Image.LANCZOS)

# Transparenz durch Weiß ersetzen:
background = Image.new("RGB", logo.size, (0, 0, 0))
logo_no_transparency = Image.alpha_composite(background.convert("RGBA"), logo)

# === Einfügen ===
qr_width, qr_height = qr_img.size
pos = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)
qr_img.paste(logo_no_transparency, pos)  # kein mask nötig

# === Speichern + Anzeigen ===
qr_img.save(output_path)
qr_img.show()