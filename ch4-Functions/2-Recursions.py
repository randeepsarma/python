def recursion(n):
    if n == 1 or n == 0:
        return 1
    return n * recursion(n - 1)


a = recursion(6)
print(a)
