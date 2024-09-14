class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        frq_arr=[0]*26
        if len(s)!=len(t):
            return False
        for c in s:
            frq_arr[ord(c)-ord('a')]+=1
        for c in t:
            frq_arr[ord(c)-ord('a')]-=1
        for frq in frq_arr:
            if frq!=0:
                return False
        return True