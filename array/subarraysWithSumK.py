class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={0:1}
        presum=0
        count=0
        for num in nums:
            presum+=num
            if presum-k in d:
                count+=d[presum-k]
            d[presum]=d.get(presum,0)+1
        return count
        