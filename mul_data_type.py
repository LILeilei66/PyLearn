# coding: utf-8
"""
乘法时, 产生位扩展：所以说 float32 * int => float64
list中, 会做位截断, 所以说 float64  => float32

"""
import torch
import numpy as np

a = torch.ones([1, 2, 2, 2]).cuda()
b = torch.ones([1, 2, 2, 2]).cuda()
i = 1
j = 1
k = 1
a[0, i, j, k] = 0.021290064
b[0, i, j, k] = 0.02129006
total = 40 * 30 * 40

a_tmp = a[0, i, j, k].data.cpu().numpy()
b_tmp = b[:, i, j, k].data.cpu().numpy()
b_tmp2 = np.around(b[:, i, j, k].data.cpu().numpy(), 3)
a_tmp2 = np.around(a[0, i, j, k].data.cpu().numpy(), 3)
a_tmp3 = a_tmp2 * total # float64, 1007.xxxxx
b_tmp3 = b_tmp2 * total # float32, 1008

a1 = int(np.around(a[0, i, j, k].data.cpu().numpy(), 3) * total)
b1 = int(np.around(b[:, i, j, k].data.cpu().numpy(), 3) * total)
print("a1: %.f" %a1)
print("b1: %.f" %b1)