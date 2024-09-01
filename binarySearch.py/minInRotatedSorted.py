class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                return nums[i]
        return ans