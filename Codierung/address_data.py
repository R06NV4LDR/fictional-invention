adr = int(input("Adressbus (Bit): "))
data = int(input("Datenbus (Bit): "))

byte = (2 ** adr) * (data // 8)
print("Größe in Bytes:", byte)
print("Größe in KiB:", byte // 1024)
