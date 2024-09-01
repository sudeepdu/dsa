def bin2dec(num):
    res=''
    # while num != 0:
    #     if num%2 == 1:
    #         res+='1'
    #     else:
    #         res+='0'
    #     num=num//2
    # return res[::-1]
    while num!=0:
        res+=num%2
        num=num//2
    return res[::-1]

num=int(input("Enter the number"))
print(f'Binary eq of {num} is {bin2dec(num)}')