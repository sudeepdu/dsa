def unionOfArrays(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    i=j=0
    unionArr=[]
    while(i<n and j<m):
        if arr1[i]<=arr2[j]:
            if len(unionArr)==0 or unionArr[-1]!=arr1[i]:
                unionArr.append(arr1[i])
            i+=1
        else:
            if len(unionArr)==0 or unionArr[-1]!=arr2[j]:
                unionArr.append(arr2[j])
            j+=1 
    while i<n:
        if unionArr[-1]!=arr1[i]:
            unionArr.append(arr1[i])
        i+=1
    while j<m:
        if unionArr[-1]!=arr2[j]:
            unionArr.append(arr2[j])
        j+=1
    return unionArr
arr1 = [1, 2, 3, 4, 5]  
arr2= [1, 2, 3, 6, 7]
print(unionOfArrays(arr1,arr2))