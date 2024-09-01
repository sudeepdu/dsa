class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxreach=0
        for i in range(len(nums)):
            if i>maxreach:
                return False
            maxreach=max(maxreach,i+nums[i])
            if maxreach>=len(nums)-1:
                return True
        return False