"""
matplotlib.pyplot 常用参数:
==========================
    1. color: {color='blue'} == {color='b'}, 另外还有 'r', 'g';
    2. marker: marker='.', 'o';
    3. inestyle: linestyle='-', '--', '-.'
添加修饰:
========
    1. 图例 legend: plt.legend(['legend name'])
    2. 轴标题 xlabel || ylabel: plt.set_xlabel('axe x')
    3. 画标题 title: plt.title('title')
legend 参数:
===========
    1. loc: {loc=0} == {loc='best'} || {loc=1} == {loc='upper right'}
    2. bbox_to_anchor: 与 loc 相结合使用.
        e.g.: (..., loc=1, bbox_to_anchor=(1,1)) => 最右上角
              (..., loc=1, bbox_to_anchor=(0,0)) => 最左上角
注:
===
    1. 对于twinx, 如果两个 ax.legend.loc 相同, 后者会覆盖前者;
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = np.sqrt(x)
y2 = x ** 2

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax1.plot(x, y1,'r'), ax1.legend(['exp'], loc='upper left')
ax2.plot(x, y2, 'b'), ax2.set_label('square')
ax2.legend(['square'], loc='upper left')

ax1.set_xlabel('axe x'), ax1.set_ylabel('y1')
ax2.set_ylabel('y2')
fig.legend(['exp', 'square'], loc=1, bbox_to_anchor=(0.9, 0.9))
plt.title('fig title')
fig.show()