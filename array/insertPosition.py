def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid-1]<target and nums[mid+1]<target:
                return mid
            elif nums[mid]>target:
                high-=1
            else:
                low+=1
nums=[1,3,5,6]
target=4
print(searchInsert(nums,target))