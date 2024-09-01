def sortedarray(arr):
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            return True
        else:
            return False
arr=[1,3,4,6,7]
print(sortedarray(arr))