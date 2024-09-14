class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st=[]
        n=len(num)
        for i in range(n):
            while st and k>0 and int(st[-1]) > int(num[i]):
                st.pop()
                k-=1
            st.append(num[i])
        while k>0:
            st.pop()
            k-=1
        result=''.join(st).lstrip('0')
        return result if result else '0'
        