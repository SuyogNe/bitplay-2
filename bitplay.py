def checkifsame(num1, num2):
    if (num1 ^ num2) == 0:
        print("The two numbers are the same")
    else:
        print("The two numbers are different")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
checkifsame(num1, num2)