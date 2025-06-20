def parse_lzw_string_no_import(s):
    tokens = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = ''
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            tokens.append(int(num))
        else:
            tokens.append(s[i])
            i += 1
    return tokens

def lzw_decode_hybrid(encoded):
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    char_to_code = {chr(i): i for i in range(dict_size)}
    code_to_char = {i: chr(i) for i in range(dict_size)}

    codes = []
    for item in encoded:
        if type(item) is str:
            codes.append(char_to_code[item])
        else:
            codes.append(item)

    result = []
    w = code_to_char[codes[0]]
    result.append(w)

    for k in codes[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            print("value error")
            return
        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        code_to_char[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return ''.join(result)

# Example usage:
encoded_str = input("Input: ")
parsed = parse_lzw_string_no_import(encoded_str)
print("Decoded:", lzw_decode_hybrid(parsed))

