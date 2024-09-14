class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        start=0
        balance=0
        result=[]
        for i, char in enumerate(s):
            if char=='(':
                balance+=1
            else:
                balance-=1
            if balance==0:
                result.append(s[start+1:i])
                start=i+1
        return ''.join(result)