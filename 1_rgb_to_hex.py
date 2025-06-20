# RGB zu HEX Umrechnung
# Eingabe: R, G, B (0–255)

r = int(input("R: "))
g = int(input("G: "))
b = int(input("B: "))

hexcode = '#{:02X}{:02X}{:02X}'.format(r, g, b)
print("HEX:", hexcode)
