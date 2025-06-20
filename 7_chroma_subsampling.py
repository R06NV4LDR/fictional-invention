# Speicherberechnung bei YCbCr mit Subsampling
# Formel:
# Y = W * H
# Cb/Cr = je nach Modus

w = int(input("Breite in Pixel: "))
h = int(input("Höhe in Pixel: "))
modus = input("Modus (4:4:4 / 4:2:2 / 4:2:0): ")

y = w * h

if modus == "4:4:4":
    cb = cr = y
elif modus == "4:2:2":
    cb = cr = (w // 2) * h
elif modus == "4:2:0":
    cb = cr = (w // 2) * (h // 2)
else:
    print("Ungueltiger Modus")
    cb = cr = 0

gesamt = y + cb + cr
mb = gesamt / (1024 * 1024)

print("Y:", y, "Bytes")
print("Cb / Cr:", cb, "Bytes je")
print("Rechnung: {} + {} + {} = {} Bytes".format(y, cb, cr, gesamt))
print("In MB:", round(mb, 2))
