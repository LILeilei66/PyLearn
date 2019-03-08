import os

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
