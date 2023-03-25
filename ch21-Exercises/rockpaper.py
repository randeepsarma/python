import random

n = random.randint(1, 3)
inp = int(input("Enter your number"))
if inp == n:
    print("Draw")
elif inp == 3 and n == 1:
    print("comp wins")
elif inp == 1 and n == 3:
    print("Player wins")
elif inp > n:
    print("player wins")
elif inp < n:
    print("comp wins")
