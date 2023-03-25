a = input("Enter the number")
print("The multiplication table of {a} is:")

b = int(a)
try:
    for i in range(1, 10):
        print(f"{a}*{i}={b*i}")
# except Exception as e:
#    print(f"Sorry we got the error {e}")
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("index Error")
