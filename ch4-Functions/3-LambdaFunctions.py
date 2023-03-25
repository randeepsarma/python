# def double(x):
#    return x * 2


double = lambda x: x**3
average = lambda x, y: (x + y) / 2


# print(double(5))
# print(average(4, 5))


def funct(num, d):
    return num + d(3)


print(f"{funct(3, double)}")
