"""
python 函数中的参数传递是 传值调用 还是 引用调用?
============================================
这个问题有两个小知识点:
(1) python 的变量是什么;
(2) python 的可更改与不可更改.

变量
----
python 的变量不存在类型, 可以理解为一个引用, 类似于 void*.
类型属于对象.

可更改与不可更改
--------------
可更改: [list, dict];
不可更改: [str, tuple, number]
e.g.,
    a = 1
    a = 2 # 产生新的 int 对象, 并指向它.

    b = [1]
    b[0] = 2 # b 的指向并无改变, 但是 b[0] 的指向发生改变.

# http://winterttr.me/2015/10/24/python-passing-arguments-as-value-or-reference/
"""
from copy import copy

def change_int(a):
    a = 2
    return a

def change_list_element(a):
    a[0] = 2
    return a

def change_value(a):
    b = a
    b[0] = 2
    return b

def change_list(a):
    b = a
    b = [2]
    return b

def change_copy_list(a):
    b = copy(a)
    b[0] = 2
    return b

if __name__ == '__main__':
    a = 1
    b = change_int(a)
    print('b: %d ; a : %d.' % (b, a)) # b: 2 ; a : 1.

    c = [1]
    d = change_list_element(c)
    print('c: {:} ; d : {:}.'.format(c, d)) # c: [2] ; d : [2].

    e = [1]
    f = change_value(e)
    print('e: {:} ; f : {:}.'.format(e, f)) # e: [2] ; f : [2].

    g = [1]
    h = change_list(g)
    print('g: {:} ; h : {:}.'.format(g, h)) # g: [1] ; h : [2].

    i = [1]
    j = change_copy_list(i)
    print('i: {:} ; j : {:}.'.format(i, j)) # i: [1] ; j : [2].

