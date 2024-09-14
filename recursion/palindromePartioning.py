class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        final=[]
        self.solve(0,s,[],final)
        return final
    

    def solve(self,ind,s,res,final):
        if ind==len(s):
            final.append(res[:])
            return
        for i in range(ind,len(s)):
            if self.isPali(s[ind:i+1]):
                res.append(s[ind:i+1])
                self.solve(i+1,s,res,final)
                res.pop()
        
    def isPali(self,k):
        return k==k[::-1]