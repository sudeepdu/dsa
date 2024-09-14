class Solution(object):
    def subArrayRanges(self, nums):
        if not nums:
            return 0
        n = len(nums)
        return self.sumMax(nums, n) - self.sumMin(nums, n)
    
    def sumMax(self, nums, n):
        ans=0
        nge = self.findnge(nums, n)
        pgee = self.findpgee(nums, n)
        for i in range(n):
            left = i - pgee[i]
            right = nge[i] - i
            ans += (left * right * nums[i])
        return ans
    
    def findnge(self, nums, n):
        nge = [n] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            st.append(i)
        return nge
    
    def findpgee(self, nums, n):
        pgee = [-1] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            if st:
                pgee[i] = st[-1]
            st.append(i)
        return pgee
    
    def sumMin(self, nums, n):
        nse = self.findnse(nums, n)
        psee = self.findpsee(nums, n)
        ans=0
        for i in range(n):
            x = nse[i] - i
            y = i - psee[i]
            ans += (x * y * nums[i])
        return ans

    def findnse(self, nums, n):
        nse = [n] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                nse[i] = st[-1]
            st.append(i)
        return nse

    def findpsee(self, nums, n):
        psee = [-1] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:
                psee[i] = st[-1]
            st.append(i)
        return psee
