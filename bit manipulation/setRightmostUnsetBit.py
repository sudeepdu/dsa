# n=4
# k=n
# pos=0
# while k:
#     if k & 1 == 0:
#         break
#     k>>=1
#     pos+=1
# print(n | 1<<pos)
def func(n):
    if n & (n+1) == 0:
        return n
    else:
        return n | (n+1)
n=int(input("Enter the number: "))
print(func(n))