"""
学习一下 functools 的使用,
具体学习如下函数:
    1. functools.partial;
    2. functools.update_wrapper;
    3. functools.wraps;
    4. functools.reduce

    未记录项:
    1. functools.cmp_to_key
    2. functools.total_ordering
    3. functools.lru_cache
    4. functools.singledispatch
ref: http://kuanghy.github.io/2016/10/26/python-functools
"""
import functools

# <editor-fold desc="1. functools.partial">
"""
:return: 函数
作用, 将 keyword 包到 func 中.
一个实例: 在 functools.wraps 中 return functools.partial(functools.update_wrappers, wrapper)
         <上例解决了 函数装饰器无法继承元信息 的问题.>
"""
print('1.')
def mult(x, y):
    return x * y
mult_y = functools.partial(mult, 10)
print(mult_y(2))

mult = functools.partial(mult, 10, 3)
print(mult())

del mult, mult_y
# </editor-fold>

# <editor-fold desc="2. functools.update_wrapper">
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
print('2.')
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

del func1, func2, wrap, wrap2
# </editor-fold>

# <editor-fold desc="3. functools.wraps">
print('3.')
import time
def using_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(time.strftime('%c'))
        return func(*args, **kwargs)
    return wrapper

@using_time
def foo(param):
    print('in foo', param)

foo('functools.wraps')
print(foo.__name__)
# </editor-fold>

# <editor-fold desc="4. functools.reduce">
"""
Equal to the builtin function reduce in py2.
"""
print('4.')
def add(x, y):
    return x + y

print(functools.reduce(add, list(range(5))))
del add
# </editor-fold>

# <editor-fold desc="5. functools.cmp_to_key">

print('5.')
data = ['hello','abc','python']
data.sort(key=len)
print(data)
# </editor-fold>

