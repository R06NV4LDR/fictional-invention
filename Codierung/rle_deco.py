def rle_decode(code):
    result = ""
    i = 0
    while i < len(code):
        char = code[i]
        count = ""
        i += 1
        while i < len(code) and code[i].isdigit():
            count += code[i]
            i += 1
        result += char * int(count)
    return result

code = input("RLE-Code eingeben: ")
decoded = rle_decode(code)
print("RLE decodiert:", decoded)
