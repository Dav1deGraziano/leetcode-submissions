class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])

        first_column = False
        first_row = False

        for i in range(m):
            if matrix[i][0]==0:
                first_column = True
        for j in range(n):
            if matrix[0][j]==0:
                first_row = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j],matrix[i][0] = 0,0
        
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(1,m):
                    matrix[i][j]=0

        for i in range(1,m):
            if matrix[i][0]==0:
                matrix[i][1:]=[0 for i in range(1,n)]
        
        if first_column:
            for i in range(m):
                matrix[i][0]=0
        if first_row:
            for j in range(n):
                matrix[0][j]=0
        
        