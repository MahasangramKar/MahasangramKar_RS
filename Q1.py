def deepest_nesting(lst):
    stack, max_d = [(lst, 1)], 1
    while stack:
        curr, d = stack.pop()
        max_d = max(max_d, d)
        for i in curr:
            if isinstance(i, list):
                stack.append((i, d + 1))
    return max_d
example = [1, [2, [3, [4, []]]], 5]
print(deepest_nesting(example))