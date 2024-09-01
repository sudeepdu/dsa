class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        st=[]
        d={}
        for num in reversed(nums2):
            while st and st[-1]<=num:
                st.pop()
            d[num]=st[-1] if st else -1
            st.append(num)
        ans=[d[num] for num in nums1]
        return ans