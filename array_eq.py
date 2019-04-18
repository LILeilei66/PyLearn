import numpy as np
a = np.array([[1,2,4]])
b = np.array([[2,3,4]])
print(a == b) # [[False False True]]

print((a == b).all()) # False, 相当于对于结果再做一次与运算.
print((a == b).any()) # True, 相当于对于结果再做一次或运算.
