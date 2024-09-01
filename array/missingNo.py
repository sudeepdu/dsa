#find missing number in array of range(0,n)
def missingNumber( arr):
    n=len(arr)
    ans=((n*(n+1))//2)-sums(arr)
    return ans
def sums(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum
arr=[0,2,3]
print(missingNumber(arr))
