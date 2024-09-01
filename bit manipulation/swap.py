def swap(a, b):
    a=a ^ b
    b=a ^ b
    a=a ^ b
    print(f'After swapping a = {a} b = {b}')

a=int(input('Enter a:'))
b=int(input('Enter b:'))
swap(a,b)