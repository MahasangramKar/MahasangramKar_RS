lst = ['a', 'b', 'c']
d = {'a': 10, 'c': 20, 'd': 40}
K = 'c'

if K in lst and K in d:
    print(d[K])
else:
    print("Key not in both")
