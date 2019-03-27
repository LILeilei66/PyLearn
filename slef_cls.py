"""
在 class 中的函数定义一共有三种方法:
    1. def func(self, *args, **kwargs)
    2. @staticmethod
       def func(*args, **kwargs)
    3. @classmethod
       def func(cls, *args, **kwargs)

@staticmethod
-------------
    可以由类名或对象名进行调用
    优点: 不需要对于整个 class 进行实例化.

"""

class a(object):
    b = 1
    def func1(self, name):
        print('--func1---')
        print('func1 name is', name)

    @staticmethod
    def func2(name):
        print('--func2---')
        print('static2 name is', name)
        a.b =2

        print('b2 is', a.b)
        a.func3(name)

    @classmethod
    def func3(cls, name):
        print('--func3---')
        print('class3 name is', name)
        print('b3 is', cls.b)
        # print('static3 is', cls.func2(name))

if __name__ == '__main__':
    A = a()
    # A.func1('as')   # func1 name is as
    # A.func2('as')
    #                 # static2 name is as
    #                 # b2 is 1
    A.func3('as')
    #                 # class3 name is as
    #                 # b3 is 1
    #                 # --func2 - --
    #                 # static2 name is as
    #                 # b2 is 1
    #                 # static3 is None
    print('=====')
    a.func2('sd')   # static2 name is sd
                    # b2 is 1
    a.func3('sd')
                    #  class3 name is sd
                    # b3 is 1
                    # --func2---
                    # static2 name is sd
                    # b2 is 1
                    # None
    a.func1(a, 'sd')# func1 name is sd
    a.func1('sd')   # TypeError: func1() missing 1 required positional argument: 'name'

