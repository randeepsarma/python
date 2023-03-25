l = [1, 2, 4, 6, 4, 3]


def cube(x):
    return x**3


newl = list(map(cube, l))
print(newl)
