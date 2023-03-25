class Employee:
    # class variable -common to all classes
    companyName = "Apple"

    def __init__(self, name, raise_amt):
        # instance variable
        self.name = name
        self.raise_amount = raise_amt

    def showDetails(self):
        print(
            f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount}"
        )


emp1 = Employee("Harry", 12)
emp1.showDetails()
