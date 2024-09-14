#next smaller element
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

#previous smaller or equal element
def findpsee(self, nums, n):
    psee = [-1] * n
    st = []
    for i in range(n):
        #add >= instead of > while comparing st[-1]] and nums[i] to write function for previous smaller element
        while st and nums[st[-1]] > nums[i]:
            st.pop()
        if st:
            psee[i] = st[-1]
        st.append(i)
    return psee

#next greater element
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

#previous greater or equal element
def findpgee(self, nums, n):
    pgee = [-1] * n
    st = []
    for i in range(n):
        #add <= instead of < while comparing st[-1]] and nums[i] to write function for greater smaller element
        while st and nums[st[-1]] < nums[i]:
            st.pop()
        if st:
            pgee[i] = st[-1]
        st.append(i)
    return pgee