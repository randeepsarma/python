class Person:
    # Below is a constructor
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    # Below is function
    def assign(self):
        return f"Name: {self.name}\nAge: {self.age}\nOccupation: {self.occupation}"


first = Person("Randeep Sarma", "18", "Farmer")
print(f"{first.assign()}")
second = Person("Rahul Das", "18", "Kheti")
print(f"{second.assign()}")
