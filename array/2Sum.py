class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        for i in range(len(nums)):
            more=target-nums[i]
            if more in hash_map:
                return i,hash_map[more]
            hash_map[nums[i]]=i