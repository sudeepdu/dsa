class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n=len(nums)
        l=r=0
        asum=0
        count=0
        while r<n:
            asum+=nums[r]
            while asum>goal:
                asum-=nums[l]
                l+=1
            count+=1
            r+=1
        return count