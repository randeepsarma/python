
x = int(input("Enter the value of x:"))
#no break statement is needed as only correct case is matched
match x:
    case 0:
        print("x is zero")

    case 4:
        print("Case is 4")

   #default cases
    case _ if(x==5):
        print(x)   
    case _ if(x>5):
        print(x,"Greater than 5")
    case _:
        print("Regular case")    
        