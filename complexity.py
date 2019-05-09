"""
时间复杂度包括对于 4 点的考虑:
1. 算法策略; 2. 编译质量; 3. 输入规模; 4. 执行速度

NP 问题:
    Non-deterministic Polynomial - 非确定多项式,
    可以在多项式时间内验证.
"""

def swap(a, b):
    # O(1)
    tmp = a
    a = b
    b = tmp

def foo2(n):
    # 1 + n + 2 * n^2 -> O(n^2)
    sum = 0 # O(1)
    for i in range(n): # O(n)
        for j in range(n): # O(n^2)
            sum += 1 # O(n^2)

def foo3(n):
    # 2 * (n-1) + 2 * (n - 1) * (2 * n) -> O(n ^ 2)
    x, y = 0, 0
    for i in range(1, n): # O(n-1)
        y += 1 # O(n-1)
        for j in range(2 * n + 1): # O((n-1)*(2*n))
            x += 1 #  O((n-1)*(2*n))

def foo4(n):
    # 4 * n + 1 -> O(n)
    a, b = 0, 1 # O(1)
    for i in range(n): # O(n)
        s = a + b # O(n)
        b = a # O(n)
        a = s # O(n)

def foo5(n):
    # 2 ^ f(n) <= n -> log(n)
    i = 1
    while i <= n:
        i = i * 2 # f(n)

def foo6(array):
    """
    输入一个长为 N 的array, 问里面sum max 是几
    :param array:
    :return:
    """
    count = 0
    N = len(array)
    for start in range(N): # O(N)
        for end in range(start + 1, N): # O(N * (N - start))
            window = array[start:end]
            sum = 0
            for value in window:
                sum += value
                count += 1
    print(count)

foo6([1,2,3,4,5]) # todo