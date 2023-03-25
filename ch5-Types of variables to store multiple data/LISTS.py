marks = [6,7,9,"HARRY",5,65,96,97,9]
print(marks)
print(marks[0])
print(marks[1])
print(marks[-3])

if 7 in marks:print("Yes")
else:print("No")

#JUMP INDEX
# From index 1 to 6 skipping 2,4
print(marks[1:6:2])


l=[100,4,65,325,3]
#sort 
"""
l.sort()
print(l)
l.sort(reverse=True)
print(l) """

#creates a new copy instead of a reference
""" 
m=l.copy()
m[0]=1
print(m)
"""

#insert an item at a particular index
""" l.insert(1,8)
print(l) """

#append one list behind another
m=[45,4,24]
l.extend(m)
print(l)