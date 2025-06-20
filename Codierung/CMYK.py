# Speicherberechnung bei YCbCr mit Subsampling (Zahleneingabe 1–3)
# Kompatibel mit TI-84 Plus CE-T Python (kein f-String)

print("Wähle Subsampling-Modus:")
print("1 = 4:4:4 (keine Farbreduktion)")
print("2 = 4:2:2 (halbierte Farbauflösung horizontal)")
print("3 = 4:2:0 (halbierte Farbauflösung horizontal & vertikal)")

modus = int(input("Modus (1-3): "))
w = int(input("Breite in Pixel: "))
h = int(input("Höhe in Pixel: "))

y = w * h

if modus == 1:
    cb = cr = y
    bezeichnung = "4:4:4"
elif modus == 2:
    cb = cr = (w // 2) * h
    bezeichnung = "4:2:2"
elif modus == 3:
    cb = cr = (w // 2) * (h // 2)
    bezeichnung = "4:2:0"
else:
    print("Ungültige Auswahl.")
    cb = cr = 0
    bezeichnung = "unbekannt"

gesamt = y + cb + cr
mb = gesamt / (1024 * 1024)

# Ausgabe mit klassischem format()
print("Modus: " + bezeichnung)
print("Y (Luminanz): " + str(y) + " Bytes")
print("Cb / Cr: " + str(cb) + " Bytes je")
print("Rechnung: " + str(y) + " + " + str(cb) + " + " + str(cr) + " = " + str(gesamt) + " Bytes")
print("= " + str(round(mb, 2)) + " MB")
