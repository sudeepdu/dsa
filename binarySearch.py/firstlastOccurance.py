class Solution(object):
    def searchRange(self, nums, target):
        f=self.first(nums,target)
        l=self.last(nums,target)
        if f==-1 or l==-1:
            return (-1,-1)
        return(f,l)
    def first(self,nums,target):
        ans=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def last(self,nums,target):
        ans=-1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=target:
                if nums[mid]==target:
                    ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans