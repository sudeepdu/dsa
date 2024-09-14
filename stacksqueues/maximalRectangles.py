class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        ht=[[0 for _ in range(col)] for _ in range(row)]
        for j in range(col):
            count=0
            for i in range(row):
                count+=int(matrix[i][j])
                if matrix[i][j]=='0':
                    count=0
                ht[i][j]=count
        maxArea=0
        for row in ht:
            area=self.findArea(row, col)
            maxArea=max(maxArea, area)
        return maxArea
    def findArea(self, row, col):
        st=[]
        maxArea=0
        for i in range(col):
            while st and row[st[-1]]>=row[i]:
                ele=row[st.pop()]
                nse=i
                pse=st[-1] if st else -1
                area=ele*(nse-pse-1)
                maxArea=max(maxArea, area)
            st.append(i)
        while st:
            ele=row[st.pop()]
            nse=col
            pse=st[-1] if st else -1
            area=ele*(nse-pse-1)
            maxArea=max(maxArea, area)
        return maxArea