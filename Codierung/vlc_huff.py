def runLengthEncodingIterative(input_str):
    output = ''

    if len(input_str) == 0:
        return output

    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            output += input_str[i - 1] + str(count)
            count = 1

    output += input_str[-1] + str(count)
    return output


input_str = input("Input: ")
print(runLengthEncodingIterative(input_str))
