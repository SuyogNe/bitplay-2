def checkifsame(num1, num2, num3):
    if (num1 ^ num2 ^ num3) == 0:
        print("The three numbers are the same")
    else:
        print("The three numbers are different")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
checkifsame(num1, num2, num3)