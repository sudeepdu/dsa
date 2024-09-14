class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final=[]
        self.helper(0, nums, [], final)
        return final
    
    def helper(self, ind, nums, res, final):
        if ind==len(nums):
            final.append(res[:])
            return
        res.append(nums[ind])
        self.helper(ind+1, nums, res, final)
        res.pop()
        self.helper(ind+1, nums, res, final)