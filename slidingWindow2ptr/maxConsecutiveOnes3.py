class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=r=0
        zeros=0
        curr=0
        maxlen=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            curr=r-l+1
            maxlen=max(curr,maxlen)
        return maxlen