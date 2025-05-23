import numpy as np
random_array = np.random.rand(5, 5)
border_elements = np.concatenate((
    random_array[0, :],
    random_array[-1, :],
    random_array[1:-1, 0],
    random_array[1:-1, -1]))
print(border_elements)
