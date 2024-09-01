#It might not be most optimal solution because it consumes extra space og O(n) since we are using hash_map
class Solution1(object):
    def majorityElement1(self, nums):
        hash_map = {}
        n = len(nums)

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        for key, value in hash_map.items():
            if value > n / 2:
                return key

        return -1
    
#We get mosty optimal solution by using Moores algorithm of voting
class Solution(object):
    def majorityElement(self, nums):
        count=0
        for i in range(len(nums)):
            if count==0:
                count+=1
                el=nums[i]
            elif nums[i]==el:
                count+=1
            else:
                count-=1
        return el


