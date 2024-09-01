def oddorev(num):
    if num and 1 == 0:
        # we can use XOR operator also
        return 'even'
    else:
        return 'odd'
num=int(input('Enter the number:'))
print(f'{num} is {oddorev(num)}')

