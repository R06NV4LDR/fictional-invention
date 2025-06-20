def twos_complement(n, bits):
    if n >= 0:
        bin_str = bin(n)[2:]  # ohne '0b'
    else:
        bin_str = bin((1 << bits) + n)[2:]  # 2er-Komplement

    # Auffüllen mit führenden Nullen
    while len(bin_str) < bits:
        bin_str = "0" + bin_str

    return bin_str

# Eingabe
num = int(input("Zahl (neg/pos): "))
bit = int(input("Bitbreite: "))

# Ausgabe
print("2er-Komplement:", twos_complement(num, bit))
