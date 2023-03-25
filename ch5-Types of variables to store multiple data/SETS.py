s = {2, 4, 2, 6}
print(s)

# order is not guanranteed
info = {"Carla", 19, False, 5.9, 19, 2, 4}
print(info)

print(type(info))

# declaring an empty set
st = set()

# declaring an empty dictionary
dict = {}

print(type(st))
print(type(dict))

# Looping through a set
for value in info:
    print(value)

# uniting sets and assigning it to a new variable
print(s.union(info))

# updating one set by putting value of one set into another ,s1=s1 +s2-s1 ^ s2
newS = s.copy()
newS.update(info)  # newS updates
print(newS)


# update a set with intersection portion of two different sets, s1=s1 ^ s2
newS1 = s.copy()
newS1.intersection_update(info)
print(newS1)

# symmetric difference update: s1=s1+s1- 2*s1^s2
newS2 = s.copy()
newS2.symmetric_difference_update(info)
print(newS2)

# symmetric difference is symmetric difference update but storing the values in a new variable instead of updating the previous one
newS3 = s.copy()

newS4 = newS3.symmetric_difference(info)
print(newS4)


# difference update -updates the original set(S1) to contain values which are not in set (S2)
newS5 = s.copy()
newS5.difference_update(info)
print(newS5)


# difference
newS6 = s.copy()
newS7 = newS6.difference(info)
print(newS7)

# add a particular value
newS7.add(5)
print(newS7)

# remove a particular item
newS7.remove(5)
print(newS7)

# delete an entire set
""" 
del newS7
print(newS7) 
"""

# clearing a set and not deleting the set
newS7.clear()
print(newS7)
