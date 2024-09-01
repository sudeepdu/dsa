def leftRotate(arr,d):
    d=d%(len(arr))
    arr[:]=arr[d:]+arr[:d]
arr=[1,2,3,4,5,6,7]
d=3
leftRotate(arr,d)
print(arr)
