class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={'a':0,'b':0,'c':0}
        l=0
        count=0
        for r in range(len(s)):
            d[s[r]]+=1
            while all(d[ch]>0 for ch in 'abc'):
                count+=len(s)-r
                d[s[l]]-=1
                l+=1
        return count