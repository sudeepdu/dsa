class Solution(object):
    def searchInsert(self, nums, target):
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)

        ans=None
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans