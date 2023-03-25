class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, department, subRole):
        Employee.__init__(self, name, id)
        self.department = department
        self.subRole = subRole

    def __str__(self):
        return f"Name:{self.name}\nId:{self.id}\nDepartment:{self.department}\nSubRole:{self.subRole}"


first = Programmer("Rohan Das", 1, "IT", "Full Stack Developer")
print(first)
