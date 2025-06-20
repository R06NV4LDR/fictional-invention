res_w = float(input("Width (px): "))
res_h = float(input("Height (px): "))
fps = float(input("FPS (Frames per second): "))
byte_per_pic = float(input("Bytes pro Pixel (z.B. 3 für RGB): "))
length = float(input("Filmlänge in Minuten: "))

# Schritt 1: Auflösung
full = res_w * res_h
print("")
print("Schritt 1: Auflösung = " + str(res_w) + " x " + str(res_h) + " = " + str(full) + " Pixel pro Bild")

# Schritt 2: Speicher pro Bild
size = full * byte_per_pic
print("Schritt 2: Speicher pro Bild = " + str(full) + " * " + str(byte_per_pic) + " = " + str(size) + " Bytes")

# Hilfsfunktion zur Ausgabe in verschiedenen Einheiten
def print_size(nr):
    print("~ Speichergrößen:")
    print("  Bytes: " + str(nr))
    print("  KB   : " + str(nr / 1000))
    print("  MB   : " + str(nr / 1000000))
    print("  GB   : " + str(nr / 1000000000))
    print("  TB   : " + str(nr / 1000000000000))

# Ausgabe der Bildgröße
print("")
print("Bildgröße:")
print_size(size)

# Schritt 3: Anzahl Bilder
frame_count = fps * 60 * length
print("")
print("Schritt 3: Gesamtanzahl Bilder = " + str(fps) + " * 60 Sek * " + str(length) + " Min = " + str(frame_count) + " Bilder")

# Schritt 4: Gesamtspeicher
size_full = size * frame_count
print("Schritt 4: Gesamtspeicher = " + str(size) + " * " + str(frame_count) + " = " + str(size_full) + " Bytes")

# Ausgabe der Filmgröße
print("")
print("Filmgröße:")
print_size(size_full)
