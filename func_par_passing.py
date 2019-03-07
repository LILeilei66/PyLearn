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

def change_int(a):
    a = 2
    return a

def change_list(a):
    a[0] = 2
    return a

if __name__ == '__main__':
    a = 1
    b = change_int(a)
    print('b: %d ; a : %d.' % (b, a)) # b: 2 ; a : 1.

    c = [1]
    d = change_list(c)
    print('c: {:} ; d : {:}.'.format(c, d)) # c: [2] ; d : [2].
