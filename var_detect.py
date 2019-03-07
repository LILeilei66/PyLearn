# -*- coding: utf-8 -*-
"""
使用 try 来判断变量是否存在.
"""

if __name__ == '__main__':
    a = 1
    try:
        a
    except:
        print('no a')

    try:
        b
    except:
        print('no b')
    """
    no b
    """