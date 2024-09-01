class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        m=len(nums1)
        n=len(nums2)
        newlen=n+m
        ind2=newlen//2
        ind1=newlen//2 - 1
        ele1=-1
        ele2=-1
        count=0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                if count==ind1:
                    ele1=nums1[i]
                if count==ind2:
                    ele2=nums1[i]
                i+=1
                count+=1
            else:
                if count==ind1:
                    ele1=nums2[j]
                if count==ind2:
                    ele2=nums2[j]
                j+=1
                count+=1
        while i<m:
            if count==ind1:
                ele1=nums1[i]
            if count==ind2:
                ele2=nums1[i]
            i+=1
            count+=1
        while j<n:
            if count==ind1:
                ele1=nums2[j]
            if count==ind2:
                ele2=nums2[j]
            j+=1
            count+=1
        if newlen%2==0:
            return (ele1+ele2)/2
        else:
            return ele2

sol=Solution()
nums1 = [1,3]
nums2 = [2]
print(sol.findMedianSortedArrays(nums1,nums2))