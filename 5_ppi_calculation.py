# PPI = Pixel pro Zoll
# Formel: PPI = Pixel / Zoll

pixel = int(input("Pixelanzahl: "))
inch = float(input("Zoll (in Inch): "))

ppi = pixel / inch
print("Rechnung: {} / {} = {:.2f} PPI".format(pixel, inch, ppi))
 # ergibt 300.0