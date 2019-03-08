"""
当调用另外一个文件夹里的脚本的时候, 相对路径究竟时相对于原脚本, 还是被调用的脚本而言的?

当前路径 . 代表的是被执行的脚本所在路径, 因此是 main.py所在路径.
解决方法: 利用 os.path.dirname(__file__) 获得包的位置路径.
    current_path = os.path.dirname(__file__)
    path = os.path.join(current_path, relative_path)
"""
from relative_path.func import func, load_txt, load_with_relative_path
import os

if __name__ == '__main__':
    path = './relative_path/test.txt'
    print(os.path.abspath(path))
    func(path) # func get file:  True
    load_txt() # load_txt get file:  False
    load_with_relative_path() # load_with_relative_path get file: True

"""
def func(path):
    print('func get file: ', os.path.isfile(path))

def load_txt():
    path = './test.txt'
    print('load_txt get file: ', os.path.isfile(path))

def load_with_relative_path():
    path = './test.txt'
    current_path = os.path.dirname(__file__)
    print('current_path: ',current_path)
    path = os.path.join(current_path, path)
    print('load_with_relative_path get file: ', os.path.isfile(path))

"""