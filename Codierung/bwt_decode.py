def bwt_decode(last_column, original_index):
    n = len(last_column)
    tuples = [(char, i) for i, char in enumerate(last_column)]
    sorted_tuples = sorted(tuples)

    next_table = [0] * n
    for i, (_, orig_i) in enumerate(sorted_tuples):
        next_table[orig_i] = i

    row = original_index - 1  # convert to 0-based index
    decoded = []
    for _ in range(n):
        char = last_column[row]
        decoded.append(char)
        row = next_table[row]
    return ''.join(decoded[::-1])


# Example usage with your image values:
bwt_str = input("Input: ")
orig_idx = int(input("index: "))
print("Decoded:", bwt_decode(bwt_str, orig_idx))

