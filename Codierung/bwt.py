def bwt_verbose(input_string):
    print("1. Schritt: Rotationen")
    n = len(input_string)
    rotations = [input_string[i:] + input_string[:i] for i in range(n)]
    for rot in rotations:
        print(rot)
    print()

    print("2. Schritt: Alphabetisch sortieren")
    table = sorted(rotations)
    for i, row in enumerate(table, 1):
        print(str(i) +" : " +row)
    print()

    print("3. Schritt: Letzte Spalte und Position des Originals")
    last_column = [row[-1] for row in table]
    original_index = table.index(input_string) + 1  # 1-based index for German explanation
    for i, row in enumerate(table, 1):
        print(str(i) + " : "+row+" -> "+row[-1])
    print("\nBWT: " + ''.join(last_column)+" oder als Position: "+str(original_index))
    print()

    # Optional: Block for D-numbered notation like 1D2R1B4E
    print("4. Schritt: Zeichen & Längen zählen (wie 1D2R1B4E)")
    result = []
    last_char = last_column[0]
    count = 1
    for c in last_column[1:]:
        if c == last_char:
            count += 1
        else:
            # Format-String entfernt: stattdessen mit str() und +
            if count > 1:
                result.append(str(count) + last_char)
            else:
                result.append(last_char)
            last_char = c
            count = 1
    # Letzten Block auch ohne f-string
    if count > 1:
        result.append(str(count) + last_char)
    else:
        result.append(last_char)

    print("".join(result))

    print("\n---\n")
    print("Letzte Spalte:", "".join(last_column))
    print("Position der Originalzeile:", original_index)

    return ''.join(last_column), original_index

# Example usage:
input_string = input("Input: ")
bwt, idx = bwt_verbose(input_string)

