# private mode - can be accessed from functions within the class
# public mode - can be accessed from functions outside the class
# protected mode - can be accessed from functions of an child class and parent class
class Employee:
    def __init__(self):
        # private variable with double dash in front
        self.__name = "Harry"


a = Employee()
# print(a.__name)

# this is called name mangling to allow easy access of private variables that have been made private by mistake
print(a._Employee__name)
