lst = [('a', 1), ('b', 2), ('a', 3)]
d = {}
for k, v in lst:
    d[k] = d.get(k, []) + [v]
print(d)
