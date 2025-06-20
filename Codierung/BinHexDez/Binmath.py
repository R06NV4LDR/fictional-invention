while True:
    print("Bin mit fractional zu Dez: 1")
    print("Bin mit fractional zu Hex: 2")
    print("Bin mit fractional zu Okt: 3")

    eingabe = input("Eingabe: ")

    if eingabe == "1":
        print("Binäre Dezimalstellen mit fractional zu Dezimal")
        # Function to convert binary to decimal
        def binary_to_decimal(binary_str):
            try:
                return int(binary_str, 2)
            except ValueError:
                return "Invalid binary number"
        # Function to convert fractional part of binary to decimal
        def fractional_binary_to_decimal(fractional_str):
            fractional_decimal = 0
            for i, digit in enumerate(fractional_str):
                fractional_decimal += int(digit) * (2 ** -(i + 1))
            return fractional_decimal

        # Accept user input
        binary_number = input("Enter a binary number (e.g., 101.11): ")

        # Split the number into integer and fractional parts
        parts = binary_number.split(".")
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else '0'

        # Convert integer part from binary to decimal
        integer_decimal = binary_to_decimal(integer_part)
        

        # Convert fractional part from binary to decimal
        fractional_decimal = fractional_binary_to_decimal(fractional_part)


        # Combine integer and fractional parts
        decimal_number = integer_decimal + fractional_decimal

        # print it human readable with a space for each 3 digits
        print("Binary " + binary_number + " in decimal is: " )
        print(decimal_number)


    elif eingabe == "2":
        print("Binär mit fractional zu Hexadezimal")
        # Function to convert binary to hexadecimal
        def binary_to_hexadecimal(binary_str):
            try:
                return hex(int(binary_str, 2)).split('x')[-1]
            except ValueError:
                return "Invalid binary number"

        # Function to convert fractional part of binary to hexadecimal
        def fractional_binary_to_hexadecimal(fractional_str):
            fractional_hexadecimal = ""
            for i, digit in enumerate(fractional_str):
                fractional_hexadecimal += hex(int(digit, 2))[-1]
            return fractional_hexadecimal

        # Accept user input
        binary_number = input("Enter a binary number (e.g., 101.11): ")

        # Split the number into integer and fractional parts
        parts = binary_number.split(".")
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else '0'

        # Convert integer part from binary to hexadecimal
        integer_hexadecimal = binary_to_hexadecimal(integer_part)

        # Convert fractional part from binary to hexadecimal
        fractional_hexadecimal = fractional_binary_to_hexadecimal(fractional_part)

        # Combine integer and fractional parts
        hexadecimal_number = integer_hexadecimal + "." + fractional_hexadecimal
        print("Binary " + binary_number + " in hexadecimal is: " )
        print(hexadecimal_number)

    elif eingabe == "3":
        print("Binär mit fractional zu Oktal")
        # Function to convert binary to octal
        def binary_to_octal(binary_str):
            try:
                return oct(int(binary_str, 2)).split('o')[-1]
            except ValueError:
                return "Invalid binary number"

        # Function to convert fractional part of binary to octal
        def fractional_binary_to_octal(fractional_str):
            fractional_octal = ""
            for i, digit in enumerate(fractional_str):
                fractional_octal += oct(int(digit, 2))[-1]
            return fractional_octal

        # Accept user input
        binary_number = input("Enter a binary number (e.g., 101.11): ")

        # Split the number into integer and fractional parts
        parts = binary_number.split(".")
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else '0'

        # Convert integer part from binary to octal
        integer_octal = binary_to_octal(integer_part)

        # Convert fractional part from binary to octal
        fractional_octal = fractional_binary_to_octal(fractional_part)

        # Combine integer and fractional parts
        octal_number = integer_octal + "." + fractional_octal
        print("Binary " + binary_number + " in octal is: " )
        print(octal_number)

    print("Nochmal? (y/n)")
    wiederholung = input("Eingabe: ")
    if wiederholung == "n":
        break
    else:
        continue