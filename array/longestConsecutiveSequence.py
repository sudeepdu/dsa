def longestSuccessiveElements(a):
    # Write your code here.
    a.sort()
    maxi=1
    cnt=1
    for i in range(1,len(a)):
        if a[i-1]==a[i]:
            continue
        if a[i-1]+1==a[i]:
            cnt+=1
        else:
            cnt=1
        maxi=max(cnt,maxi)
    return maxi
