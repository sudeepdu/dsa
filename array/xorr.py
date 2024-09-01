def solve( A, B):
    cnt=0
    for i in range(len(A)):
        xorr=0
        for j in range(i,len(A)):
            xorr=xorr^A[j]
            if xorr==B:
                cnt+=1
    return cnt
A = [5, 6, 7, 8, 9]
B = 5
print(solve(A,B))