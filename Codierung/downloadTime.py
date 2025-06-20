res_w = float(input("Width (px): "))
res_h = float(input("Height (px): "))
fps = float(input("FPS (Frames per second): "))
byte_per_pic = float(input("Bytes pro Pixel (z. B. 3 für RGB): "))
length = float(input("Filmlänge in Minuten: "))

# Berechnung Pixel pro Bild
full = res_w * res_h
print(f"\nSchritt 1: Auflösung = {res_w} x {res_h} = {full} Pixel pro Bild")

# Berechnung Speicher pro Bild
size = full * byte_per_pic
print(f"Schritt 2: Speicher pro Bild = {full} * {byte_per_pic} = {size} Bytes")

def print_size(nr: float):
    print("~ Speichergrößen:")
    print("  Bytes:", nr)
    print("  KB   :", nr / 1_000)
    print("  MB   :", nr / 1_000_000)
    print("  GB   :", nr / 1_000_000_000)
    print("  TB   :", nr / 1_000_000_000_000)

print("\nBildgröße:")
print_size(size)

# Berechnung Filmgröße
frame_count = fps * 60 * length
print(f"\nSchritt 3: Gesamtanzahl Bilder = {fps} FPS * 60 Sek * {length} Min = {frame_count} Bilder")

size_full = size * frame_count
print(f"Schritt 4: Gesamtspeicher = {size} Bytes/Bild * {frame_count} Bilder = {size_full} Bytes")

print("\nFilmgröße:")
print_size(size_full)

# Berechnung Datenr
