# PPI Berechnung (pixels per inch)
# Formel: Pixel / Zoll

def calc_ppi(pixels, inches):
    return round(pixels / inches, 2)

# Beispiel
print(calc_ppi(3000, 10))  # ergibt 300.0