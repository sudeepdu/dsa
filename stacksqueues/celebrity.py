def findCelebrity(matrix):
    top=0
    bottom=len(matrix)-1
    while top<bottom:
        if matrix[top][bottom]==1:
            top+=1
        elif matrix[bottom][top]==1:
            bottom-=1
        else:
            top+=1
            bottom-=1
    if top!=bottom:
        return -1
    for i in range(len(matrix)):
        if i!=top:
            if matrix[top][i]!=0 or matrix[i][top]!=1:
                return -1
    return top