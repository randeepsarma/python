op = int(input("Enter operation:"))
strn = input("Enter the string:")
if len(strn) < 3:
    str = reversed(strn)
    print(*strn)
elif op == 1:  # coding
    # breaking the string
    newSt = strn[1 : len(strn)] + strn[0]
    newSt = "xyz" + newSt + "abc"
    print(newSt)
else:  # decoding
    strn = strn[3 : len(strn) - 3]
    strn = strn[len(strn) - 1] + strn[0 : len(strn) - 1]
    print(strn)
