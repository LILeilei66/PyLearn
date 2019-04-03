"""
int type 会影响数据的加减.
"""
import warnings
warnings.filterwarnings('ignore')
import numpy as np
a = np.uint8(130)
b = np.uint8(126)
print(a + b, type(a + b)) # 0 <class 'numpy.uint8'>
print(int(a) + int(b)) # 256
print(b - a, type(b - a)) # 252 <class 'numpy.uint8'>
print(int(b)-int(a)) # -4