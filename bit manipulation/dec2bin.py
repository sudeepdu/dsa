def bin2dec(str):
    num=0
    for i in range (len(str)):
        if str[i] == 1:
            num+=pow(2,i)
    return num
str=input("Enter the binary number\n")
print(f'Decimal eq of {str} is ')