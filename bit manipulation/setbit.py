def setbit(n,k):
    n=n^(1<<k)
    return n
n=int(input('Enter the number: '))
k=int(input('Enter the position of bit to be set: '))
print(f'{n} After setting the bit at position {k} is {setbit(n,k)}')