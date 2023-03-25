class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The name of the employee is {self.name} str"

    # if __str__ if not present then __repr__ runs
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"

    def __call__(self):
        print("Hey I am good")
