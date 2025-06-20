
def decimal_to_binary(n):
    b = bin(n)
    if b.startswith("0b"):
        return b[2:]
    return b

def decimal_to_hex(n):
    h = hex(n)
    if h.startswith("0x"):
        return h[2:]
    return h

def binary_to_decimal(b):
    try:
        return int(b, 2)
    except:
        return "Ungültige Binärzahl"

def hex_to_decimal(h):
    try:
        return int(h, 16)
    except:
        return "Ungültige Hexzahl"

def main():
    while True:
        print("=== Umrechnungsmenü ===")
        print("1: Dezimal zu Binär")
        print("2: Dezimal zu Hexadezimal")
        print("3: Binär zu Dezimal")
        print("4: Hexadezimal zu Dezimal")
        print("0: Beenden")

        choice = input("Wahl: ")

        if choice == "1":
            dec = int(input("Dezimalzahl: "))
            print("Binär:", decimal_to_binary(dec))
        elif choice == "2":
            dec = int(input("Dezimalzahl: "))
            print("Hexadezimal:", decimal_to_hex(dec))
        elif choice == "3":
            b = input("Binärzahl: ")
            print("Dezimal:", binary_to_decimal(b))
        elif choice == "4":
            h = input("Hexadezimalzahl: ")
            print("Dezimal:", hex_to_decimal(h))
        elif choice == "0":
            print("Beendet.")
            break
        else:
            print("Ungültige Eingabe.")

main()