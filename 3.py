def twoodd(arr,size):
    num=arr[0]
    x=0
    y=0
    setbit=0
    for i in range(1, size):
        num = num ^ arr[i]

    setbit = num & ~(num-1)
    for i in range(size):
        if (arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    print("The two odd occurring elements are: ", x, " and ", y)

arr = []
arrsize = int(input("Enter the no. of items: "))
for i in range(0, arrsize):
    ans= int(input("Enter the number: "))
    arr.append(ans)
print(twoodd(arr, arrsize))