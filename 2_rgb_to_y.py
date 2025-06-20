# RGB zu Y (Luminanz) – Helligkeit
# Y = 0.299·R + 0.587·G + 0.114·B

r = int(input("R: "))
g = int(input("G: "))
b = int(input("B: "))

y = 0.299 * r + 0.587 * g + 0.114 * b
print("Y (Luminanz):", round(y, 2))
