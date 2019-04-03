"""
int type 会影响数据的加减.
"""
import numpy as np
a = np.uint8(130)
b = np.uint8(126)
print(a + b, type(a + b)) # 0 <class 'numpy.uint8'>
print(b - a, type(b - a)) # 252 <class 'numpy.uint8'>
