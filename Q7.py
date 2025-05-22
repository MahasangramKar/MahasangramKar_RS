def flatten_chars(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result

char_list = ['a', ['b', 'c'], 'd', ['e'], 'f']
flattened = flatten_chars(char_list)
print("Original:", char_list)
print("Flattened:", flattened)
