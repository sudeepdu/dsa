#minimum number of bits to be flipped to convert A to B
def fun(a,b):
    xorr=a^b
    count=0
    while xorr > 1:
        count+=xorr & 1
        xorr>>=1
        if xorr==1:
            count+=1
    return count
a=int(input('Enter A: '))
b=int(input('Enter B: '))
print(f'minimum number of bits to be flipped to convert A to B are {fun(a,b)}')