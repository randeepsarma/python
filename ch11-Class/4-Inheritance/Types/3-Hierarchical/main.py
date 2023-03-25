class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer:
    department = "IT"

    def __init__(self, name, id, subRole):
        Employee.__init__(self, name, id)

        self.subRole = subRole

    def __str__(self):
        return f"Name:{self.name}\nId:{self.id}\nDepartment:{self.department}\nSubRole:{self.subRole}"


class Finance:
    department = "Finance"

    def __init__(self, name, id, subRole):
        Employee.__init__(self, name, id)

        self.subRole = subRole

    def __str__(self):
        return f"Name:{self.name}\nId:{self.id}\nDepartment:{self.department}\nSubRole:{self.subRole}"


coder1 = Programmer("Rahul D", 1, "Full Stack Developer")
finance1 = Finance("Anita Das", 2, "C.A")
print(coder1)
print(finance1)
