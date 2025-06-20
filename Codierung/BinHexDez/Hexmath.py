while True:
    print("Hex mit fractional zu Dez: 1")
    print("Hex mit fractional zu Bin: 2")
    print("Hex mit fractional zu Okt: 3")

    eingabe = input("Eingabe: ")

    if eingabe == "1":
        print("Hexadezimal Dezimalstellen mit fractional zu Dezimal")

        # Function to convert hexadecimal to decimal
        def hexadecimal_to_decimal(hex_str):
            try:
                return int(hex_str, 16)
            except ValueError:
                return "Invalid hexadecimal number"

        # Function to convert fractional part of hexadecimal to decimal
        def fractional_hexadecimal_to_decimal(fractional_str):
            fractional_decimal = 0
            for i, digit in enumerate(fractional_str):
                fractional_decimal += int(digit, 16) * (16 ** -(i + 1))
            return fractional_decimal

        # Accept user input
        hexadecimal_number = input("Enter a hexadecimal number (e.g., 1.A): ")

        # Split the number into integer and fractional parts
        parts = hexadecimal_number.split(".")
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else "0"

        # Convert integer part from hexadecimal to decimal
        integer_decimal = hexadecimal_to_decimal(integer_part)

        # Convert fractional part from hexadecimal to decimal
        fractional_decimal = fractional_hexadecimal_to_decimal(fractional_part)

        # Combine integer and fractional parts
        decimal_number = integer_decimal + fractional_decimal
        print("Hexadecimal " + hexadecimal_number + " in decimal is: ")
        print(decimal_number)

    elif eingabe == "2":
        print("Hexadezimal mit fractional zu Binär")

        # Function to convert hexadecimal to binary
        def hexadecimal_to_binary(hex_str):
            try:
                return bin(int(hex_str, 16)).split("b")[-1]
            except ValueError:
                return "Invalid hexadecimal number"

        # Function to convert fractional part of hexadecimal to binary
        def fractional_hexadecimal_to_binary(fractional_str):
            fractional_binary = ""
            for i, digit in enumerate(fractional_str):
                fractional_binary += bin(int(digit, 16))[-1]
            return fractional_binary

            # Accept user input

        hexadecimal_number = input("Enter a hexadecimal number (e.g., 1.A): ")

        # Split the number into integer and fractional parts
        parts = hexadecimal_number.split(".")
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else "0"

        # Convert integer part from hexadecimal to binary
        integer_binary = hexadecimal_to_binary(integer_part)

        # Convert fractional part from hexadecimal to binary
        fractional_binary = fractional_hexadecimal_to_binary(fractional_part)

        # Combine integer and fractional parts
        binary_number = integer_binary + "." + fractional_binary
        print("Hexadecimal " + hexadecimal_number + " in binary is: ")
        print(binary_number)

    elif eingabe == "3":
        print("Hexadezimal mit fractional zu Oktal")

        # Function to convert hexadecimal to octal
        def hexadecimal_to_octal(hex_str):
            try:
                return oct(int(hex_str, 16)).split("o")[-1]
            except ValueError:
                return "Invalid hexadecimal number"

        # Function to convert fractional part of hexadecimal to octal
        def fractional_hexadecimal_to_octal(fractional_str):
            fractional_octal = ""
            for i, digit in enumerate(fractional_str):
                fractional_octal += oct(int(digit, 16))[-1]
            return fractional_octal

            # Accept user input

        hexadecimal_number = input("Enter a hexadecimal number (e.g., 1.A): ")

        # Split the number into integer and fractional parts
        parts = hexadecimal_number.split(".")
        integer_part = parts[0]
        fractional_part = parts[1] if len(parts) > 1 else "0"

        # Convert integer part from hexadecimal to octal
        integer_octal = hexadecimal_to_octal(integer_part)

        # Convert fractional part from hexadecimal to octal
        fractional_octal = fractional_hexadecimal_to_octal(fractional_part)

        # Combine integer and fractional parts
        octal_number = integer_octal + "." + fractional_octal
        print("Hexadecimal " + hexadecimal_number + " in octal is: ")
        print(octal_number)

    
    print("Nochmal? (y/n)")
    wiederholung = input("Eingabe: ")
    if wiederholung == "n":
        break
    else:
        continue
