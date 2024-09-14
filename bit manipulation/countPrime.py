class Solution(object):
    def countPrimes(self, n):
        if n<=2:
            return 0
        prime = [True for i in range(n)]

        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        cnt=0
        for p in range(2, n):
            if prime[p]:
                cnt+=1
        return cnt