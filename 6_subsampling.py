# Speicherersparnis durch Chroma Subsampling
# Faktor:
# 4:4:4 = 1.0, 4:2:2 = 0.67, 4:2:0 = 0.5

original = float(input("Originalgroesse (MB): "))
modus = input("Modus (4:4:4 / 4:2:2 / 4:2:0): ")

if modus == "4:4:4":
    faktor = 1.0
elif modus == "4:2:2":
    faktor = 0.67
elif modus == "4:2:0":
    faktor = 0.5
else:
    print("Ungueltiger Modus")
    faktor = 1.0

neu = original * faktor
print("Rechnung: {:.2f} * {:.2f} = {:.2f} MB".format(original, faktor, neu))
