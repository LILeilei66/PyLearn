import itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable) # return tuple of n=2 independent iterators.
    next(b, None)
    return zip(a, b), a, b

def tee_src_code(iterable, n=2):
    import collections
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                newval = next(it)       # fetch a new value and
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)


if __name__ == '__main__':
    result, a, b = pairwise([1,5,2,6,3])
    for value in result:
        print(value)
    print(list(a), list(b))
    for value in list(a):
        print(value)
    for value in list(b):
        print(value)