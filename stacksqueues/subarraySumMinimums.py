class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        nse=self.nseFunc(arr, n)
        psee=self.pseeFunc(arr, n)
        ans=0
        mod=int(1e9+7)
        for i in range(n):
            x=nse[i]-i
            y=i-psee[i]
            ans+=(x*y*arr[i])%mod
            ans%=mod
        return ans

    def nseFunc(self, arr, n):
        nse=[n]*n
        st=[]
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                nse[i]=st[-1]
            st.append(i)
        return nse

    def pseeFunc(self, arr, n):
        psee=[-1]*n
        st=[]
        for i in range(n):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                psee[i]=st[-1]
            st.append(i)
        return psee