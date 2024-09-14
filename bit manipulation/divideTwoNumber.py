class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == divisor:
            return 1 
        sign=1
        INT_MIN, INT_MAX = -2**31, 2**31 - 1 
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign=-1
        n=abs(dividend)
        d=abs(divisor)
        quotient=0
        while n>=d:
            cnt=0
            while n>=(d<<cnt+1):
                cnt+=1
            quotient+=1<<cnt
            n-=d<<cnt
        quotient*=sign
        if quotient<INT_MIN:
            return INT_MIN
        if quotient>INT_MAX:
            return INT_MAX
        return quotient