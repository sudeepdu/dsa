def jumpGame2(nums):
    l,r=0,0
    jumps=0
    while r<len(nums):
        reach=0
        for i in range(l,r+1):
            reach=max(reach,i+nums[i])
        l=r+1
        r=reach
        jumps+=1
    return jumps
nums=[2,3,1,4,1,1,2]
print(jumpGame2(nums))