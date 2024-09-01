arr=[i for i in range(1,101)]
arr.pop(23)
n=len(arr)
xorr=0
for i in range(n):
    xorr=xorr^arr[i]^(i+1)
print(xorr^(n+1))