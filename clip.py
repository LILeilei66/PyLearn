"""
当超过某范围时, saturate.
"""
import numpy as np
import torch

a = np.arange(0,10) # [0 1 2 3 4 5 6 7 8 9]

b = np.clip(a, a_min=2, a_max=8) # [2 2 2 3 4 5 6 7 8 8]
c = torch.from_numpy(a)
c = torch.clamp(c, 2, 8) # tensor([2, 2, 2, 3, 4, 5, 6, 7, 8, 8], dtype=torch.int32)

print(a)
print(b)
print(c)
