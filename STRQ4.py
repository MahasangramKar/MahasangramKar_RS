my_dict = {
    'a': [1, 2, 3],
    'b': [2, 3, 4],
    'c': [4, 5]
}

unique_values = set()
new_dict = {}

for key in my_dict:
    new_list = []
    for val in my_dict[key]:
        if val not in unique_values:
            new_list.append(val)
            unique_values.add(val)
    new_dict[key] = new_list

print(new_dict)
