import numpy as np
arr = np.array([1, 2, 3])
arr_even = np.append(arr, [x for x in [4, 5, 6] if x % 2 == 0])
print(arr_even)
