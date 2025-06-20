import math

def add_bin(a, b, bits):
    dec_sum = int(a, 2) + int(b, 2)
    max_val = 2 ** bits
    overflow = dec_sum >= max_val
    truncated = dec_sum % max_val
    bin_str = bin(truncated)[2:]  # Ohne '0b'
    # ggf. führende Nullen auffüllen
    while len(bin_str) < bits:
        bin_str = "0" + bin_str
    return bin_str, dec_sum, overflow

# Eingaben
a = input("1. Binär: ")
b = input("2. Binär: ")

# Dezimalsumme berechnen
sum_dec = int(a, 2) + int(b, 2)
suggested_bits = int(math.ceil(math.log(sum_dec + 1) / math.log(2)))

print("Dezimalsumme:", sum_dec)
print("Empfohlene Bitbreite:", suggested_bits)

bits = int(input("Gewünschte Bitbreite: "))

# Berechnung
res, real_sum, overflow = add_bin(a, b, bits)

print("--------- Ergebnis ---------")
print("Binär-Summe (gekürzt auf Bitbreite):", res)
print("Dezimalsumme:", str(real_sum))
print("Überlauf auf " + str(bits) + " Bit:", overflow)
