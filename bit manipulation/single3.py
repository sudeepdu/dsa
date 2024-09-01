def func(arr):
    xorr=0
    for i in range(len(arr)):
        xorr=xorr^arr[i]
    rightMost=(xorr&(xorr-1))&xorr
    b1=0
    b2=0
    for i in range(len(arr)):
        if arr[i]&rightMost==0:
            b1=b1^arr[i]
        else: 
            b2=b2^arr[i]
    return (b1,b2)
arr=[4, 2, 4, 5, 2, 3, 3, 1]
print(func(arr))