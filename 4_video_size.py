# Video-Speicherplatz (unkomprimiert)
# Formel: W * H * bpp * fps * Dauer / 8 / 1024^2

w = int(input("Breite in Pixel: "))
h = int(input("Höhe in Pixel: "))
bpp = int(input("Bits pro Pixel (z. B. 24): "))
fps = int(input("FPS (z. B. 30): "))
dauer = int(input("Dauer in Sekunden: "))

bytes_total = w * h * bpp * fps * dauer / 8
mb = bytes_total / (1024 * 1024)

print("Rechnung: {}*{}*{}*{}*{} /8 = {:.0f} Bytes".format(w, h, bpp, fps, dauer, bytes_total))
print("In MB:", round(mb, 2))
