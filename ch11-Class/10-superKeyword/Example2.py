class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


Rohan = Employee("Rohan Das", "428")
Harry = Programmer("Harry", "2345", "Python")
print(Harry.name)
print(Harry.id)
print(Harry.lang)
