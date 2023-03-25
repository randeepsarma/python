class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod  # class method as alternative constructors
    def fromStr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

    def showDetails(self):
        print(f"Name is {self.name} and salary is {self.salary}")


e1 = Employee("Harry", 12000)
e1.showDetails()
string = "John-12000"
e2 = Employee.fromStr(string)
e2.showDetails()
