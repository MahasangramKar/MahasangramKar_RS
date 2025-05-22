def intersection(a, b):
    return list(set(a) & set(b))

list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 5, 2]
result = intersection(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Intersection (no duplicates):", result)
