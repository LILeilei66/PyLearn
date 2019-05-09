"""
问题阐释:
    之前对于装饰器的理解仅在于 静态函数(@staticmethod), 与 类函数(@clsmethod),
    具体来说, 是关于内存和删除的问题.

    在进行 functools.update_wrapper 的过程中, 发现是通过装饰器进行实现的,
    具体来说,
        def wrap(func):
            def call_it(*args, **kwargs):
                print('calling', func.__name__)
                return func
            return call_it

        @wrap
        def func():
            print('func')

        func() # 先输出 'calling func\n' 再输出 'func'

    所以说, 当使用修饰器的时候, 是先call一遍修饰器函数么？他们之间的调用关系是怎样的呢？
"""

# <editor-fold desc="0. py 函数可以作为参数进行传递">
def foo():
    print('foo')

def bar(func):
    func()

bar(foo)
del bar, foo
# </editor-fold>

# <editor-fold desc="1. 函数实现装饰器原理">
"""
本质: 函数 或 类
作用: 让其他 函数 或 类 增加额外功能, 因此 :return: 函数/类 对象.
常用场景: 插入日志, 性能测试, 事务处理, 缓存, 权限校验 等场景.
"""
import time
def foo():
    print('in foo')

# 欲新加功能 using time 至 foo
# method 1:
"""问题: 此时实际调用时不再是使用 foo, 而是使用 using_time"""
def using_time(func):
    print(func.__name__, time.strftime('%c'))

# method 2:
print('1.2')
def using_time(func):
    """
    using_time 是一个装饰器, 它将 func 函数包裹其中,
    :param func:
    :return: 函数 wrapper
    """
    def wrapper():
        print(func.__name__, time.strftime('%c'))
        func()
        return func
    return wrapper

foo_wrapped = using_time(foo)
foo_wrapped()

del foo, using_time, foo_wrapped
# </editor-fold>

# <editor-fold desc="2. 函数原理的 @ 包装">
print('2.')
def using_time(func):
    """
    using_time 是一个装饰器, 它将 func 函数包裹其中,
    :param func:
    :return: 函数 wrapper
    """
    def wrapper():
        print(func.__name__, time.strftime('%c'))
        func()
        return func
    return wrapper

@using_time
def foo():
    print('in foo')
foo()

del foo, using_time
# </editor-fold>

# <editor-fold desc="3. 带参函数的装饰实现">
print('3.')
def foo(arg):
    print('in foo', arg)

def using_time(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, 'with', str(*args), str(**kwargs), time.strftime('%c'))
        return func(*args, **kwargs)
    return wrapper

@using_time
def foo(arg):
    print('in foo', arg)

foo('3. 带参函数的装饰实现')

del foo, using_time
# </editor-fold>

# <editor-fold desc="4. 带参装饰器实现">
"""
实现原理: parameterized_decorator 其实是对于原装饰器的一个函数封装 
         :return: 装饰器
应用场景: 在装饰其中指定日志的等级.
"""
def parameterized_decorator(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(param)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@parameterized_decorator('4.')
def foo(arg):
    print('in foo', arg)

foo('带参装饰器实现')
del foo, parameterized_decorator
# </editor-fold>

# <editor-fold desc="5. 类装饰器实现">
"""
实现原理: 使用类装饰器主要依靠类的 __call__ 方法
"""
print('5. ')
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('call foo')
        self._func()
        print('end foo')

@Foo
def bar():
    print('in bar')
bar()

del Foo, bar
# </editor-fold>

# <editor-fold desc="6. 装饰器的问题">
"""
装饰器会抹去原函数的元信息(元信息 := 信息的信息), 包括 docstring, __name__, dict.
e.g.:  
"""
print('6.')
def using_time(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, time.strftime('%c'))
        return func(*args, **kwargs)
    return wrapper

@using_time
def foo(param):
    print('in foo', param)

foo('装饰器的问题')
print(foo.__name__) # wrapper

del foo, using_time
# </editor-fold>

# <editor-fold desc="7. 元信息拷贝">
"""
利用 functools.wraps 完成.
实现方式: 将 decorator 中的 wrapper function 进行修饰.
问题: functools.update_wrapper 是什么? 
"""
print('7.')
import functools

def using_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, time.strftime("%c"))
        return func(*args, **kwargs)
    return wrapper

@using_time
def foo(param):
    print('in foo', param)

foo('元信息拷贝')
print(foo.__name__)
del foo, using_time
# </editor-fold>

# <editor-fold desc="7.1. functools.update_wrapper">
"""
在 functools.learn.py 中最后 :return: update_wrapper(wrapper, func)
那么, update_wrapper 与 wraps 的区别是什么呢?
二者无本质区别, 在源码中有:
def wraps(wrapped, assigned, updated):
    return partial(update_wrapper, wrapped,
                   assigned, updated)
"""
print('7.1.')
def using_time(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, time.strftime("%c"))
        return func(*args, **kwargs)
    return functools.update_wrapper(wrapper, func)

@using_time
def foo(param):
    print('in foo', param)

foo('functools.update_wrapper')
print(foo.__name__)
del foo, using_time
# </editor-fold>

# <editor-fold desc="同时定义多个装饰器">
"""
一个函数可以同时定义多个装饰器, 调用顺序为从里到外.
@a              |  f = a(b(c(f)))
@b              |
@c              |
def f():        |
    pass        |
"""
# </editor-fold>