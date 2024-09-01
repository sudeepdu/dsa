def pow2(num):
    if num & num-1 != 0:
        return 'NO'
    else:
        return 'Yes'
    
num=int(input('Enter the number:'))
print(pow2(num))