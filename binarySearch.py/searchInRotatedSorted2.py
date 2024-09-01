#Contains duplicate so implement using linear search
def func(nums,target):
    for num in nums:
        if num==target:
            return True
    return False