def gen(n):
    pro = 1
    for i in range(1, n):
        pro = pro * i
        yield pro


g = gen(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def fibonacci(n):
    prev = 0
    next = 1
    for i in range(0, n):
        temp = next + prev
        prev = next
        next = temp
        yield temp


fibSeq = fibonacci(10)
print(next(fibSeq))
print(next(fibSeq))
print(next(fibSeq))
print(next(fibSeq))
print(next(fibSeq))
print(next(fibSeq))
