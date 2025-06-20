# Speicherplatz unkomprimiertes RGB-Bild
# Formel: Breite * Höhe * 3 Bytes (1 Byte pro Farbe)
# Ergebnis in MB

def image_size(width, height):
    return round(width * height * 3 / (1024 * 1024), 2)

# Beispiel
print(image_size(1920, 1080))  # ca. 5.93 MB