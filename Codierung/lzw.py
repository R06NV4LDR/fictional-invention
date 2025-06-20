def lzw_encode_inline(input_string):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ""
    output = []

    for c in input_string:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            # Output previous part
            if len(w) == 1:
                output.append(w)
            else:
                # Output the dictionary code for w (if it's not a single char)
                output.append(str(dictionary[w]))
            # Output the current char if not part of the code
            # Add new substring to the dictionary
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    # Output the last code or character
    if w:
        if len(w) == 1:
            output.append(w)
        else:
            output.append(str(dictionary[w]))
    return "".join(output)

# Example usage:
input_string = input("Input: ")
result = lzw_encode_inline(input_string)
print("LZW-Transformation: "+input_string +" wird zu "+result)

