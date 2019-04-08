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
    # 2 * (n-1) todo
    x, y = 0, 0
    for i in range(1, n): # O(n-1)
        y += 1 # O(n-1)
        for j in range(2 * n + 1): # O((n-1)*(2*n))
            x += 1 #  O((n-1)*(2*n))
