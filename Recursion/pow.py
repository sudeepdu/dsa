class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        nn=n
        if nn<0:
            nn*=-1
        result=1
        while nn>0:
            if nn%2:
                result*=x
                nn-=1
            else:
                x*=x
                nn//=2
        return result if n>0 else 1/result