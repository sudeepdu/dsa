def fun(x):
    if x<0:
        return False
    else:
        original=x
        rem=0
        rev=0
        while x>0:
            rem=x%10
            rev=(rev*10)+rem
            x=x//10
    return rev==original
    
x=int(input('Enter: '))
print(fun(x))