x = 4


def funct():
    global x
    x += 1
    print(x)


print(x)
funct()
print(x)
