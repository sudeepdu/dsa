#Recursive backtracking
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board=[['.' for _ in range(n)] for _ in range(n)]
        final=[]
        self.helper(0,board,n,final)
        return final

    def helper(self,col,board,n,final):
        if col==n:
            final.append([''.join(row) for row in board])
            return
        for row in range(n):
            if self.isSafe(row,col,n,board):
                board[row][col]='Q'
                self.helper(col+1,board,n,final)
                board[row][col]='.'

    def isSafe(self,row,col,n,board):
        rowdup=row
        coldup=col
        for c in range(col):
            if board[row][c]=='Q':
                return False
        row=rowdup
        col=coldup
        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        row=rowdup
        col=coldup
        while row<n and col>=0:
            if board[row][col]=='Q':
                return False
            row+=1
            col-=1
        return True