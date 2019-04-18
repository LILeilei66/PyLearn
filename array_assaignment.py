from numpy import zeros as npzeros
"""
假设有 一个list a, 使得 b = a
当修改 b[idx] a[idx]同样修改, 因为本质上是修改list里面所point的那个位置.
"""
a = npzeros((4,4))
a[3,2:4] = 1
print(a)
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 1. 1.]]
"""