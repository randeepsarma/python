dic = {344: "Harry", 56: "Shubham", 678: "Zakir"}
dic1 = {34: "Larry", 6: "Raktim", 8: "Hussein"}

print(dic[678])  # accessing values

print(dic.keys())  # accessing keys
print(dic.values())  # accessing values

# interating through keys
for key in dic.keys():
    print(key)

# iterating through key and value
for key, value in dic.items():
    print(f"{key}:{value}")


# update
dic2 = dic.copy()
dic2.update(dic1)
print(dic2)

# clear
dic2.clear()
print(dic2)

# pop key value pair with key=6
dic2.update(dic1)
dic2.pop(34)
print(dic2)


# pop only last item
dic2.update(dic1)
print(dic2)
dic2.popitem()
print(dic2)

# delete key word
""" dic2.update(dic1)
del dic2
print(dic2) """

# delete a particular key value pair
dic2.clear()
dic2.update(dic1)
del dic2[34]
print(dic2)
