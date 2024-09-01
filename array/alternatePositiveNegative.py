#This is my intution 
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsp=[]
        numsn=[]
        for i in range(len(nums)):
            if nums[i]>0:
                numsp.append(nums[i])
            else:
                numsn.append(nums[i])
        j=k=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=numsp[j]
                j+=1
            else:
                nums[i]=numsn[k]
                k+=1
        return nums