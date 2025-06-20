# Unkomprimiertes RGB-Bild
# Formel: Breite * Höhe * 3 Bytes

w = int(input("Breite in Pixel: "))
h = int(input("Höhe in Pixel: "))
b = int(input("Bytes pro Pixel (z.B. 3 bei RGB): "))

bytes_total = w * h * b
mb = bytes_total / (1024 * 1024)

print("Rechnung: {} * {} * {} = {} Bytes".format(w, h, b, bytes_total))
print("In MB:", round(mb, 2))
