class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


One = Employee("Rohan", 23)
One.showDetails()
Two = Programmer("Soham", 25)
Two.showDetails()
