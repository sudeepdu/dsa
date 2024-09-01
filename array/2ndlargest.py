def func(arr,n):
    lar=arr[0]
    slar=-1
    for i in range(n):
        if arr[i]>lar:
            slar=lar
            lar=arr[i]
        elif arr[i]>slar and arr[i]<lar:
            slar=arr[i]
    return slar
arr=[]
n=int(input('No of ele in arr: '))
for i in range(n):
    arr.append(int(input()))
print(f'Second largest ele in an arr is {func(arr,n)}')