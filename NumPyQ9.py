import numpy as np
# Slow way
arr = np.array([])
for i in range(10000):
    arr = np.append(arr, i)

# Faster way
lst = []
for i in range(10000):
    lst.append(i)
arr_concat = np.concatenate([np.array(lst)])
