def convert():
    mode = input("Modus (bin/dec/hex): ")
    val = input("Wert: ")

    if mode == "bin":
        print("Dez:", int(val, 2))
        print("Hex:", hex(int(val, 2)))
    elif mode == "dec":
        print("Bin:", bin(int(val)))
        print("Hex:", hex(int(val)))
    elif mode == "hex":
        print("Bin:", bin(int(val, 16)))
        print("Dez:", int(val, 16))
convert()
