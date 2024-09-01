#return the number which appears odd number of times in an gib=ven array
def func(arr):
    ans=0
    for i in range (len(arr)):
        ans=ans ^ arr[i]
    return ans
arr=[1,4,3,4,1]
print(f'Number which appears odd number of times in given array is {func(arr)}')