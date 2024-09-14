class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final=[]
        nums.sort()
        self.helper(0, nums, [], final)
        return final
    
    def helper(self, ind, nums, res, final):
        final.append(res[:])
        for i in range(ind,len(nums)):
            if i!=ind and nums[i]==nums[i-1]:
                continue
            res.append(nums[i])
            self.helper(i+1, nums, res, final)
            res.pop()
            