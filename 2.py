def oddocurring(arr):
    res=0
    for element in arr:
        res = res ^ element

    return res

arr=[]
n=int(input("Enter the array size: "))

while (n):
    num = int(input("Enter the number: "))
    arr.append(num)
    n -= 1
print("The odd occurring element is: ", oddocurring(arr))
