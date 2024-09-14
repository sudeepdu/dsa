class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        l=0
        r=len(num)-1
        while r>=l:
            if int(num[r])%2==1:
                return num[l:r+1]
            r-=1
        return ""