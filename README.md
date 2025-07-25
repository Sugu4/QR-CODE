
# QR-Code Generator mit Logo-Einbindung

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
 dein-projekt/
 ┣  qr_mit_logo.py         # Hauptskript zur Erstellung des QR-Codes
 ┣  logoSG.png             # Dein eigenes Logo (quadratisch, transparent oder ohne)
 ┣  qr_mit_logo.png        # Das Ergebnis – QR-Code mit integriertem Logo
 ┗  README.md              # Diese Datei
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

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Du darfst es frei verwenden, verändern und veröffentlichen.

---

## Autor

**Süleyman Gümüs**  

---

## MIT License

Steht unter der [MIT-Lizenz](./LICENSE).
