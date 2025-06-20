def rle_encode(text):
    result = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1
    result += text[-1] + str(count)
    return result

text = input("Text eingeben: ")
encoded = rle_encode(text)
print("RLE codiert:", encoded)
