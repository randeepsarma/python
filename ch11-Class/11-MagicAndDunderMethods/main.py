from emp import Employee

e = Employee("Harry")

# __str__ in Employee("Harry") runs.If __str__ is not present,it fallbacks into __repr__ and calls the function
print(e)
# prints __str__ in Employee
print(str(e))
# prints __repr__ in Employee
print(repr(e))
# prints __call__ in Employee
e()
