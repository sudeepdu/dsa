class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return n-1
        low=1
        high=n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid+1]:
                high=mid-1
            else:
                low=mid+1
                