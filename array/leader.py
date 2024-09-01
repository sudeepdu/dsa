def superiorElements(a):
    # Write your code here.
    ans=[]
    maxi=-2**31-1
    for i in range(len(a)-1,-1,-1):
        if a[i]>maxi:
            ans.append(a[i])
            maxi=a[i]
    return ans
a = [1, 2, 3, 2]
print(superiorElements(a))
