# RGB zu HEX Umrechnung
# Jeder Wert 0–255 wird in 2-stellige Hex-Zahl umgewandelt

r = int(input("R (0–255): "))
g = int(input("G (0–255): "))
b = int(input("B (0–255): "))

# Rechnung anzeigen
print("Rechnung: R={:02X}, G={:02X}, B={:02X}".format(r, g, b))

# Ergebnis
hexcode = '#{:02X}{:02X}{:02X}'.format(r, g, b)
print("HEX-Farbcode:", hexcode)
