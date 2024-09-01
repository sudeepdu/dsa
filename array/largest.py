def largest(arr):
    lar=arr[0]
    for i in range (len(arr)-1):
        if arr[i+1]>lar:
            lar=arr[i+1]
    return lar
arr=[1,56,78,43,23,34,12]
print(largest(arr))