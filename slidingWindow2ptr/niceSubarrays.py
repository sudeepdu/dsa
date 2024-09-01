class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=[num%2 for num in nums]
        d={0:1}
        presum=count=0
        for num in nums:
            presum+=num
            if presum-k in d:
                count+=d[presum-k]
            d[presum]=d.get(presum,0)+1
        return count