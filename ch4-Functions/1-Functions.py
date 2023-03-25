"""
def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)
def printGreater(a, b):
    if a > b:
        print(a)
    elif b >= a:
        print(b)
# calculateGmean(12, 12)
printGreater(1, 2)
"""


# takes a tuple
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i

    return sum


print(average(5, 6))
