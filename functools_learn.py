"""
学习一下 functools 的使用,
具体学习如下函数:
    1. functools.partial;
    2. functools.update_wrapper;
"""
import functools

# <editor-fold desc="functools.partial">
"""
:return: 函数
作用, 将 keyword 包到 func 中.
"""
def mult(x, y):
    return x * y
mult_y = functools.partial(mult, 10)
print(mult_y(2))

mult = functools.partial(mult, 10, 3)
print(mult())
# </editor-fold>

# <editor-fold desc="functools.update_wrapper">
"""
产生原因: 弥补 partial 所构造的 func 中没有 ['__name__' || '__doc__' || '__module__' || '__dict__']
         这些 attribute 的问题.
注: 此 func 多用于装饰器函数, 以确保被装饰的保留原理的属性.

实现方式: 
    WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
    WRAPPER_UPDATES = ('__dict__')
    def update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
        for attr in assigned:
            setattr(wrapper, attr, getattr(wrapped, attr)
        for attr in updated:
            getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
        return wrapper
"""

def wrap(func):
    def call_it(*args, **kwargs):
        print('calling', func.__name__)
        return func(*args, **kwargs)
    return call_it

def wrap2(func):
    def call_it(*args, **kwargs):
        print('calling', func.__name__)
        return func(*args, **kwargs)
    return functools.update_wrapper(call_it, func)

@wrap
def func1():
    print('func1')

@wrap2
def func2():
    print('func2')

func1()
func2()

print(func1.__name__)
print(func2.__name__)
func2.ca
# </editor-fold>