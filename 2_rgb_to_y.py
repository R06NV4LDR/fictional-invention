# RGB zu Y (Luminanz)
# Formel: Y = 0.299*R + 0.587*G + 0.114*B

r = int(input("R (0–255): "))
g = int(input("G (0–255): "))
b = int(input("B (0–255): "))

y = 0.299 * r + 0.587 * g + 0.114 * b
print("Rechnung: 0.299*{} + 0.587*{} + 0.114*{} = {:.2f}".format(r, g, b, y))
print("Y (Luminanz):", round(y, 2))
