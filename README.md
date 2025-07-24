
# 🔳 QR-Code Generator mit Logo-Einbindung

Mit diesem Python-Skript kannst du in wenigen Schritten QR-Codes generieren – **inklusive eigenem Logo in der Mitte**. Ideal für persönliche Webseiten, Bewerbungen, Visitenkarten oder Marketingprojekte.

---

## Funktionen

- Erstellt QR-Codes für jede beliebige URL
- Automatische Einbindung eines Logos in der Mitte
- Farblich neutral (schwarz auf weiß) für maximale Lesbarkeit
- QR-Code bleibt dank Fehlerkorrektur auch mit Logo zuverlässig scanbar

---

## Projektübersicht

```bash
📦 dein-projekt/
 ┣ 📄 qr_mit_logo.py         # Hauptskript zur Erstellung des QR-Codes
 ┣ 🖼️ logoSG.png             # Dein eigenes Logo (quadratisch, transparent oder ohne)
 ┣ 🖼️ qr_mit_logo.png        # Das Ergebnis – QR-Code mit integriertem Logo
 ┗ 📄 README.md              # Diese Datei
```

---

## Voraussetzungen

- **Python 3.x**
- Die folgenden Python-Pakete:

```bash
pip install qrcode[pil]
```

---

## Verwendung

1. **Projekt klonen oder herunterladen**

2. **Logo einfügen**  
   Lege dein Logo als `logoSG.png` im Projektverzeichnis ab.  
   → Empfehlung: quadratisch, ca. 60–100 px

3. **URL im Skript anpassen**  
   Öffne `qr_mit_logo.py` und ändere die Ziel-URL in Zeile 7:

   ```python
   url = "https://deine-webseite.de"
   ```

4. **Skript ausführen**

   ```bash
   python qr_mit_logo.py
   ```

   ✅ Dein QR-Code wird gespeichert als `qr_mit_logo.png` und automatisch angezeigt.

---

## Anpassungen

- **Logo-Größe:**  
  Passe den Wert in dieser Zeile an:

  ```python
  logo = logo.resize((60, 60), Image.LANCZOS)
  ```

- **Farben:**  
  Standard ist Schwarz auf Weiß. Ändere bei Bedarf:

  ```python
  qr.make_image(fill_color="black", back_color="white")
  ```

- **Fehlerkorrektur:**  
  Im Skript ist `ERROR_CORRECT_H` aktiviert – dies erlaubt größere Logos ohne Scanfunktion zu verlieren.

---

## Beispielanwendung

![qr_code_preview](qr_mit_logo.png)

---

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Du darfst es frei verwenden, verändern und veröffentlichen.

---

## 👤 Autor

**Süleyman Gümüs**  

---

MIT License

Copyright © 2025 Süleyman Gümüs

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
of this software and associated documentation files (the 'Software'), to use, copy, modify, merge, publish, distribute, sublicense, and to permit persons to whom the Software is furnished to do any of the foregoing.
with the Software without restriction, including, without limitation, the rights
to use, copy, modify, merge, publish, distribute, sublicense and of the Software, and to permit persons to whom the Software is
furnished, to do so, subject to the following conditions:

The above copyright notice and this permission notice must be included in all
copies or substantial portions of the Software.

The Software is provided 'as is', without warranty of any kind, express or
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGE OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
Out of or in connection with the software or the use or other dealings in the
SOFTWARE.