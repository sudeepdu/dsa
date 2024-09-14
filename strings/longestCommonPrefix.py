class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        min_length=float('inf')
        for s in strs:
            if len(s)<min_length:
                min_length=len(s)
        
        low,high =0, min_length
        while low<=high:
            mid=(low+high)//2
            if all(s.startswith(strs[0][:mid]) for s in strs):
                low=mid+1
            else:
                high=mid-1
        return strs[0][:high]