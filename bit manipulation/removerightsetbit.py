def func(n):
    return n & (n-1)
n=int(input('Enter the number: '))
print(f'Number after removing the right most set bit is {func(n)}')