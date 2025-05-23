import numpy as np
a = np.array([[6,1,1], [4,-2,5], [2,8,7]])
det_manual = (
    a[0,0]*(a[1,1]*a[2,2] - a[1,2]*a[2,1]) -
    a[0,1]*(a[1,0]*a[2,2] - a[1,2]*a[2,0]) +
    a[0,2]*(a[1,0]*a[2,1] - a[1,1]*a[2,0])
)
print(det_manual)
