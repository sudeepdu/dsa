class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        l=r=0
        maxlen=0
        curr=0
        d=dict()
        while r<n:
            if s[r] in d and d[s[r]]>=l:
                l=d[s[r]]+1
            d[s[r]]=r
            curr=r-l+1
            maxlen=max(maxlen,curr)
            r+=1
        return maxlen