import time


def usingWhile():
    i = 0
    while i < 5000:
        i += 1
        print(i)


def usingFor():
    for i in range(5000):
        print(i)


start1 = time.time()
usingWhile()
end1 = time.time() - start1
start2 = time.time()
usingFor()
end2 = time.time() - start2
print(end1)
print(end2)

time.sleep(3)
print("This is printed after 3 seconds")
