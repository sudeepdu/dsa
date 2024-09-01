def maxi(nums):
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            count=0
        maximum=max(count,maximum)
    return maximum
        