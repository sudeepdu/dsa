class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        low = 1
        high = len(nums) - 2

        while low <= high:
            mid = (low + high) // 2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid%2==0 and nums[mid]==nums[mid-1]) or (mid%2==1 and nums[mid]==nums[mid+1]):
                high=mid-1
            else:
                low=mid+1
