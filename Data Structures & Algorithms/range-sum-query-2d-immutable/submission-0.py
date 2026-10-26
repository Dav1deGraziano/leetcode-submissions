class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        m,n = len(matrix),len(matrix[0])
        self.matrix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            crt_row_sum = 0
            for j in range(n):
                crt_cell_sum = matrix[i][j] + crt_row_sum
                crt_row_sum += matrix[i][j]
                if i-1>=0:
                    crt_cell_sum += self.matrix[i-1][j]
                self.matrix[i][j] = crt_cell_sum
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2]
        if row1-1>=0 and col1-1>=0:
            ans += -self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]
        elif row1-1>=0:
            ans -= self.matrix[row1-1][col2]
        elif col1-1>=0:
            ans -= self.matrix[row2][col1-1]
        
        
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)