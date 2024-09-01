#No extra space
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l=m-1
        r=0
        while r<n and l>=0:
            if nums2[r]>nums1[l]:
                break
            else:
                nums2[r],nums1[l]=nums1[l],nums2[r]
            l-=1
            r+=1
        nums1[:]=sorted(nums1[:m])+nums1[m:]
        nums2.sort()
        i=m
        j=0
        while j<n:
            nums1[i]=nums2[j]
            i+=1
            j+=1

        