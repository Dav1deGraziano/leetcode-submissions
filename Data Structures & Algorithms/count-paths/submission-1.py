class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m==1 and n>=1:
            return 1
        elif n==1 and m>=1:
            return 1

        grid = [[0 for j in range(n)] for i in range(m)]
        grid[m-1][n-1] = 1

        k = n-2

        while k>=0:
            i,j = m-1,k
            while i>=0 and j<=n-1:
                if i+1<=m-1:
                    grid[i][j] += grid[i+1][j]
                if j+1<=n-1:
                    grid[i][j] += grid[i][j+1]
                i,j = i-1,j+1
            k -= 1

        k = m-2

        while k>=0:
            i,j = k,0
            while i>=0 and j<=n-1:
                if i+1<=m-1:
                    grid[i][j] += grid[i+1][j]
                if j+1<=n-1:
                    grid[i][j] += grid[i][j+1]
                i,j = i-1,j+1
            k -= 1

        print(grid)

        return grid[0][0]


        