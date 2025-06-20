# Speicherbedarf Video (unkomprimiert)
# Formel: Breite * Höhe * Farbtiefe (bpp) * fps * Dauer / (8 * 1024 * 1024)
# 8 für Bits zu Byte, 1024^2 für Byte zu MB

def video_size(width, height, bpp, fps, duration):
    return round(width * height * bpp * fps * duration / (8 * 1024 * 1024), 2)

# Beispiel: 1920x1080, 24 bit, 30 fps, 60 Sek.
print(video_size(1920, 1080, 24, 30, 60))