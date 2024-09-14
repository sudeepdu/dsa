#Can be implemented using next smaller and previous smaller functions nut takes extra space and traversal
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        st=[]
        maxArea=0
        for i in range(n):
            while st and heights[st[-1]]>=heights[i]:
                ele=heights[st.pop()]
                nse=i
                pse=st[-1] if st else -1
                area=ele*(nse-pse-1)
                maxArea=max(maxArea, area)
            st.append(i)
        while st:
            ele=heights[st.pop()]
            nse=n
            pse=st[-1] if st else -1
            area=ele*(nse-pse-1)
            maxArea=max(maxArea, area)
        return maxArea