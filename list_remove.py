"""
list + remove 的锁问题.
问题原因:
--------
    list 当删掉一个元素时, 所有元素前移.
解决方法:
--------
    1. 倒序遍历;
    2. while loop;
    3. filter(lambda)
    4. 复制list;
    5. 列表解析.
"""
if __name__ == '__main__':
    """
    list = [1, 2, 3, 4]
    for i in list: 
        print(i) 
        if i < 3:
            list.remove(i)
    print(list) # [2, 3, 4]

    '''
    1 [1, 2, 3, 4]
    3 [2, 3, 4] 因为, 当删除 2 后, 元素全部前移, 于是 list[1] 为 3.
    4 [2, 3, 4]
    '''

    list = [1, 2, 3, 4]
    for i in range(len(list)):
        print(i, list[i]) # IndexError: list index out of range.
        # 因为list实际长度变小, 但是循环次数是按照原长度进行.
        try:
            if list[i] < 3:
                list.remove(list[i])
        except IndexError:
            print('at %d, list index out of range' % i)
    print(list)
    """
    # ===============================================================================
    # 1. 解法一: while loop
    # ===============================================================================
    list = [1, 2, 3, 4]
    i = 0
    while i < len(list): # while 循环时 每次会检验上限的值.
        if list[i] < 3:
            list.remove(list[i])
            i -= 1
        i += 1
    print(list) # [3, 4]

    # ===============================================================================
    # 2. 解法二：倒序循环遍历
    # ===============================================================================
    list = [1, 2, 3, 4]
    for i in range(len(list)-1, -1, -1):
        print(i, list[i])
        if list[i] > 3:
            list.remove(list[i])
    print(list) # [1, 2]
    """
    | 1 | 2 | 3 |   | 1 | 2 |
    |---|---|---| => |---|---|
    |(0)|(1)|(2)*|  |(0)|(1)*|
    """

    # ===============================================================================
    # 3. 解法三：遍历拷贝的list, 操作原始的list
    # ===============================================================================
    list = [1,2,3,4]
    for i in list[:]: # list[:] 是对 list 的一个拷贝, 在拷贝上遍历, 剔除掉原始的数据.
        if i < 3:
            list.remove(i)
    print(list) # [3, 4]

    # ===============================================================================
    # 4. 解法四：filter + lambda
    # ===============================================================================
    list = [1,2,3,4]
    list = filter(lambda x: x > 2, list)
    for i, data in enumerate(list):
        print(data)
    # 3,4

    # ===============================================================================
    # 5. 解法五：列表解析
    # ===============================================================================
    list = [1,2,3,4]
    list = [x for x in list if x > 2]
    print(list) # [3, 4]