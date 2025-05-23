import numpy as np
checkerboard = np.indices((8, 8)).sum(axis=0) % 2
print(checkerboard)
