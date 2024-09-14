class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for c in s:
            if c=='(' or c=='{' or c=='[':
                st.append(c)
            else:
                if not st:
                    return False
                if (st[-1]=='(' and c==')') or (st[-1]=='{' and c=='}') or (st[-1]=='[' and c==']'):
                    st.pop()
                else:
                    return False
        return len(st)==0