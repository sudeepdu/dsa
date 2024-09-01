#check if an array is sorted and rotated
def func(arr,n):
    count=0
    for i in range(n):
        if arr[i]>arr[(i+1)%n]:
            count+=1
    if count>1:
        return False
    else:
        return True
arr=[3,4,5,1,2]
print(func(arr,len(arr)))