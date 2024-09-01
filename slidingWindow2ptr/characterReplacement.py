class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        l=0
        maxf=0
        maxlen=0
        d={}
        for r in range(n):
            d[s[r]]=d.get(s[r],0)+1
            maxf=max(maxf,d[s[r]])
            while ((r-l+1)-maxf)>k:
                d[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen
        