class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("John", 30)

# converts class variables into a dictionary
print(p.__dict__)

# used to provide information about data types in python
print(help(Person))
