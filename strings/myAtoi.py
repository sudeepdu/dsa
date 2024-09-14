class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        r=len(s)
        sign=1
        INT_MAX=2**31-1
        INT_MIN=-2**31
        ans=0

        while l<r and s[l]==' ':
            l+=1
        if l<r and (s[l]=='-' or s[l]=='+'):
            sign=-1 if s[l]=='-' else 1
            l+=1
        while l<r and s[l].isdigit():
            digit=int(s[l])
            if ans>(INT_MAX-digit)//10:
                return INT_MAX if sign==1 else INT_MIN
            ans=ans*10 + digit
            l+=1
        return ans*sign