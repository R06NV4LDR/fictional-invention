def run_length_encoding(input_str):
    if len(input_str) == 0:
        print("Leere Eingabe.")
        return ""

    output = ""
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            print(input_str[i - 1], "kommt", count, "mal vor")
            output += input_str[i - 1] + str(count)
            count = 1

    # letztes Zeichen verarbeiten
    print(input_str[-1], "kommt", count, "mal vor")
    output += input_str[-1] + str(count)

    print("Ergebnis:", output)
    return output

# Eingabeaufforderung
text = input("Text: ")
run_length_encoding(text)
