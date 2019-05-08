"""
面对函数编程 与 面对对象编程
"""
from functools import reduce

square = lambda x: x * x
for i in range(5):
    print(square(i))
print(list(map(square, list(range(5)))))

odd = lambda x: x % 2
print(list(filter(odd, list(range(5)))))

customer_sum = lambda x, y: x + y
print(reduce(customer_sum, list(range(5))))

pr = lambda str : str
num_pr = lambda x: ((x == 1) and pr('one')) \
                or ((x == 2) and pr('two')) \
                or (pr('else'))
print(list(map(num_pr, list(range(1, 4)))))