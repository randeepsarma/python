def funct1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Printed only when some error occurs")
        return 0
    finally:
        """printed regardless of success or error and after return statement"""
        print("Always executed")


x = funct1()
print(x)
