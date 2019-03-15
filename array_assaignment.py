from numpy import array as nparray
from numpy import zeros as npzeros

a = npzeros((4,4))
a[3,2:4] = 1
print(a)
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 1. 1.]]
"""