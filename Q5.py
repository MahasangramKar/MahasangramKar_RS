def compress(text):
    result = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        if count >= 3:
            result += text[i] + str(count)
        else:
            result += text[i] * count
        i += 1
    return result

s = "aaabbcccddddeeeeffffg"
compressed = compress(s)
print("Original:", s)
print("Compressed:", compressed)
