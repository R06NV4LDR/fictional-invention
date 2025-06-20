# Chroma Subsampling Rechner für TI-84 (z. B. 4:2:0)
# Rechnet den ungefähren Speicherbedarf eines Bildes mit YCbCr-Sampling
# Farbtiefe: 8 Bit (1 Byte) pro Kanal

def chroma_subsampling_bytes(width, height, mode='4:2:0'):
    y = width * height  # Luminanz (Y) bleibt immer gleich

    if mode == '4:4:4':
        cb = cr = y  # Keine Reduktion
    elif mode == '4:2:2':
        cb = cr = (width // 2) * height  # Horizontal halbiert
    elif mode == '4:2:0':
        cb = cr = (width // 2) * (height // 2)  # Horizontal + vertikal halbiert
    else:
        return "Ungültiges Format"

    total_bytes = y + cb + cr
    total_mb = round(total_bytes / (1024 * 1024), 2)

    print("Y (Luminanz):", y, "Bytes")
    print("Cb / Cr:", cb, "Bytes je")
    print("Gesamt:", total_bytes, "Bytes =", total_mb, "MB")
    return total_mb

# Beispiel: Full HD mit 4:2:0
chroma_subsampling_bytes(1920, 1080, '4:2:0')
