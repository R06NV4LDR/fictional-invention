while True:
    print("Wähle aus:")
    print("Dez to Bin: 1")
    print("Dez zu Hex: 2")
    print("Bin mit fractional zu Dez: 3")
    print("Hex mit fractional zu Dez: 4")
    print("Hex mit fractional zu Bin: 5")
    print("Bin mit fractional zu Hex: 6")
    print("Dez zu Oct: 7")

    eingabe = input("Eingabe: ")

    # also accepts fractional decimal number and convert them
    if eingabe == "1":
        print("Dezimal zu Binär")
        # Function to convert decimal to binary
        def decimal_to_binary(decimal_number):
            try:
                return bin(decimal_number).split('b')[-1]
            except ValueError:
                return "Invalid decimal number"
        # Accept user input
        decimal_input = input("Enter a decimal number (e.g., 255.2): ")
        decimal_number = float(decimal_input)
        # Split the number into integer and fractional parts
        parts = decimal_input.split(".")
        integer_part = int(parts[0])
        fractional_part = float("0." + parts[1]) if len(parts) > 1 else 0
        # Convert from decimal to binary
        integer_binary = decimal_to_binary(integer_part)
        fractional_binary = ""
        while fractional_part > 0:
            fractional_part *= 2
            fractional_binary += str(int(fractional_part))
            fractional_part -= int(fractional_part)
        # add 0 to /4
        if len(integer_binary) % 4 != 0:
            integer_binary = "0" * (4 - len(integer_binary) % 4) + integer_binary
        # add space for each 4 bits
        integer_binary = ' '.join(integer_binary[i:i+4] for i in range(0, len(integer_binary), 4))
        binary_number = integer_binary + "." + fractional_binary
    

        print("Decimal " + str(decimal_number) + " in binary is: ")
        print(binary_number)
        

    elif eingabe == "2":
        print("Dezimal zu Hexadezimal")
        # Function to convert decimal to hexadecimal
        def decimal_to_hexadecimal(decimal_number):
            try:
                return hex(decimal_number).split('x')[-1]
            except ValueError:
                return "Invalid decimal number"
        # Accept user input
        decimal_input = input("Enter a decimal number (e.g., 255.3): ")
        decimal_number = float(decimal_input)
        parts = decimal_input.split(".")
        decimal_number = int(parts[0])
        fractional_part = float("0." + parts[1]) if len(parts) > 1 else 0
        # Convert from decimal to hexadecimal
        hexadecimal_number = decimal_to_hexadecimal(decimal_number)
        fractional_hexadecimal = ""
        while fractional_part > 0:
            fractional_part *= 16
            fractional_hexadecimal += str(hex(int(fractional_part)))[-1]
            fractional_part -= int(fractional_part)
        # space for each 2 bits
        hexadecimal_number = ' '.join(hexadecimal_number[i:i+2] for i in range(0, len(hexadecimal_number), 2))
        hexadecimal_number = hexadecimal_number + "." + fractional_hexadecimal
        # Display the result
        print("Decimal " + str(decimal_number) + " in hexadecimal is: ")
        print(hexadecimal_number)

    elif eingabe == "3":
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
        print("Binary " + binary_number + " in decimal is: " )
        print(decimal_number)

    elif eingabe == "4":
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
        fractional_part = parts[1] if len(parts) > 1 else '0'

        # Convert integer part from hexadecimal to decimal
        integer_decimal = hexadecimal_to_decimal(integer_part)

        # Convert fractional part from hexadecimal to decimal
        fractional_decimal = fractional_hexadecimal_to_decimal(fractional_part)

        # Combine integer and fractional parts
        decimal_number = integer_decimal + fractional_decimal
        print("Hexadecimal " + hexadecimal_number + " in decimal is: " )
        print(decimal_number)

    elif eingabe == "5":
        print("Hexadezimal mit fractional zu Binär")
        # Function to convert hexadecimal to binary
        def hexadecimal_to_binary(hex_str):
            try:
                return bin(int(hex_str, 16)).split('b')[-1]
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
        fractional_part = parts[1] if len(parts) > 1 else '0'

        # Convert integer part from hexadecimal to binary
        integer_binary = hexadecimal_to_binary(integer_part)

        # Convert fractional part from hexadecimal to binary
        fractional_binary = fractional_hexadecimal_to_binary(fractional_part)

        # Combine integer and fractional parts
        binary_number = integer_binary + "." + fractional_binary
        print("Hexadecimal " + hexadecimal_number + " in binary is: " )
        print(binary_number)

    elif eingabe == "6":
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

    elif eingabe == "7":
        print("Dezimal zu Octal")
        # Function to convert decimal to octal
        def decimal_to_octal(decimal_number):
            try:
                return oct(decimal_number).split('o')[-1]
            except ValueError:
                return "Invalid decimal number"
        # Accept user input
        decimal_input = input("Enter a decimal number (e.g., 255.2): ")
        decimal_number = int(decimal_input)

        # Convert from decimal to octal
        octal_number = decimal_to_octal(decimal_number)
        # Display the result
        print("Decimal " + str(decimal_number) + " in octal is: ")
        print(octal_number)

    
    print("run again? ""/n")
    eingabe = input("Eingabe: ")
    if eingabe == "":
        continue
    elif eingabe == "n":
        break
    else:
        print("Invalid input")
        break

