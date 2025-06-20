while True:
    print("Dez to Bin: 1")
    print("Dez zu Hex: 2")
    print("Dez zu Okt: 3")

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
        print("Dezimal zu Oktal")
        # Function to convert decimal to octal
        def decimal_to_octal(decimal_number):
            try:
                return oct(decimal_number).split('o')[-1]
            except ValueError:
                return "Invalid decimal number"
        # Accept user input
        decimal_input = input("Enter a decimal number (e.g., 255.3): ")
        decimal_number = float(decimal_input)
        parts = decimal_input.split(".")
        decimal_number = int(parts[0])
        fractional_part = float("0." + parts[1]) if len(parts) > 1 else 0
        # Convert from decimal to octal
        octal_number = decimal_to_octal(decimal_number)
        fractional_octal = ""
        while fractional_part > 0:
            fractional_part *= 8
            fractional_octal += str(oct(int(fractional_part)))[-1]
            fractional_part -= int(fractional_part)
        # space for each 3 bits
        octal_number = ' '.join(octal_number[i:i+3] for i in range(0, len(octal_number), 3))
        octal_number = octal_number + "." + fractional_octal
        # Display the result
        print("Decimal " + str(decimal_number) + " in octal is: ")
        print(octal_number)


    print("Nochmal? (y/n)")
    wiederholung = input("Eingabe: ")
    if wiederholung == "n":
        break
    else:
        continue