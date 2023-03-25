# walrus operator allows usto assign a value to a variable within an expression

""" 
a = True
print(a := False) 
"""
""" 
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

 """
foods = list()
while food := input("What food do you like") != quit:
    foods.append(food)
