class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)
        n = len(matrix[0])

        if m==1:
            return matrix[0]
        elif n==1:
            return [matrix[i][0] for i in range(m)]
        elif m==2:
            return matrix[0]+matrix[1][::-1]
        elif n==2:
            return matrix[0] + [matrix[i][1] for i in range(1,m)]+[matrix[-1][0]]+[matrix[i][0] for i in range(m-2,0,-1)]
        else:
            return matrix[0] + [matrix[i][-1] for i in range(1,m)]+[matrix[-1][j] for j in range(n-2,-1,-1)]+[matrix[i][0] for i in range(m-2,0,-1)] + self.spiralOrder([row[1:-1] for row in matrix[1:-1]])


        