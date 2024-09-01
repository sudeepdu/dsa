# s={1,2,3,4,5,6}
# for i in list(s):
#     s.discard(i)
# print(s)


# for i in range(6):
#     for j in range(i):
#         print('*', end=" ")
#     print()

# list_1=["2",2,3,"ab",5]
# del list_1[2]
# print(list_1)

# nums=[2,3,4,5,6,7]
# for i in nums:
#     nums.pop()
# print(nums)

# lst1=[1,2,3]
# lst2=[4,6]
# newlst=[]
# for i,j in zip(lst1,lst2):   when too many iterables are being iterated
#     newlst.append(i+j)
# print(newlst)


# x='dt'
# print('a'.join(x))  'a' is inserted inbetween the characters

# output: 'dat'

# for x='dth'
# output: datah


# i=1
# while i<5:
#     print(i, end=',')
#     i+=1
#     if i==3:
#         break
# else:
#     print(0)

# x=[1,2,3]
# y=x[:]
# y[0]=5
# print(x,y)

# x=2
# def test():
#     global x
#     x+=3
#     return x
# print(x,test(),test())


# n=int(input())
# s=['.' for i in range(n)]
# k=[s for i in range(n)]
# print(k)
# print(type(k))

# list1=['p','y','t','h','o','n']
# for i in list1:
#     list1.append(i.upper())
# print(list)

# a={1:'a',2:'b',3:'c'}
# for i in a:
#     print(i,end=',')

# a=['NTH',[4,3,5,6]]
# print(a[0][1],a[1][3])

# a={1:'a',2:'b',3:'c'}
# b=a.copy()
# b[1]=4
# print(a)


# TypeError: 'tuple' object does not support item assignment
# a=[1,2,3]
# b=tuple(a)
# b[0]=7
# print(b)

# a={1:'a',2:'b',3:'c'}
# for i,j in a.items():
#     print(i,j,end=' ')

# lst=['python','django']
# lst.extend('ui')
# print(lst)

