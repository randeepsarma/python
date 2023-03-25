"""
name ="Abhishek"
for i in name: 
    print(i)
    if(i == 'A'):
        print('This is a start') 
"""

"""
colors = ['Red','Green','Blue','Yellow']
for color in colors:
    #print(color)
    for index in color:
        print(index)
"""
"""
for k in range(0,10):
    print(k)
"""

# for loop with break and else statement
for k in range(0, 10, 2):
    if k > 4:
        break
    print(k)
else:
    print("Sorry no i")

# for loop with else statement
for k in range(0, 10, 2):
    print(k)
else:
    print("Sorry no i")
