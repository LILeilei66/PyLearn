"""
当 flatten 以后, 如何可以回到原来 2D || 3D 的状态?
在 numpy 和 torch 中进行尝试.
"""
import numpy as np
import torch

origin_mat2 = [[1,2,3],[4,5,6],[7,8,9]]
"""
1,2,3
4,5,6
7,8,9
"""
origin_mat3 = [[[1,2],[3,4]],
                [[5,6],[7,8]]
              ]
"""
1,2 | 5,6
3,4 | 7,8
"""
# <editor-fold desc="np 2d">
origin = np.array(origin_mat2)
origin = origin.flatten() # [1 2 3 4 5 6 7 8 9]
rec = np.resize(origin, (3,3))
"""
1,2,3
4,5,6
7,8,9
"""
# </editor-fold>


# <editor-fold desc="np 3d">
origin = np.array(origin_mat3)
origin = origin.flatten() # [1 2 3 4 5 6 7 8]
rec = np.resize(origin, (2,2,2))
"""
1,2 | 5,6
3,4 | 7,8
"""
# </editor-fold>

# <editor-fold desc="torch 2d">
origin = torch.tensor(origin_mat2)
origin = origin.flatten() # tensor([1, 2, 3, 4, 5, 6, 7, 8, 9])
rec = torch.reshape(origin, (3,3))
"""
tensor([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
"""
# </editor-fold>


origin = torch.tensor(origin_mat3)
origin = origin.flatten() # tensor([1, 2, 3, 4, 5, 6, 7, 8])
rec = torch.reshape(origin, (2,2,2))
"""
tensor([[[1, 2],
         [3, 4]],

        [[5, 6],
         [7, 8]]])
"""
