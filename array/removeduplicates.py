#Remove duplicate in an sorted array


#brute force

# def func(arr):
#     arrset=set()
#     for i in range(len(arr)):
#         arrset.add(arr[i])
#     return arrset
# arr=[1,1,2,3,4,4,5,6,7,7]
# print(func(arr))

# opt

def func(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1
arr=[1,1,2,3,4,4,5,6,7,7]
k=func(arr)
for i in range(k):
    print(arr[i],' ')