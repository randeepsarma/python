l = [1, 2, 4, 6, 4, 3]


def funct(a):
    return a > 4


newl = filter(funct, l)
print(*newl)
