#find the XOR of number from L to R
#before doing this get to know about XOR from 1 to N and use that function
def func(l,r):
    ans=xorr(l-1) ^ xorr(r)
    print(ans)
def xorr(n):
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    elif n % 4 == 3:
        return 0
    else:
        return n
l=int(input('Enter L: '))
r=int(input('Enter R: '))
func(l,r)