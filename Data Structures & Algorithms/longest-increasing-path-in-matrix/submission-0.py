class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m,n = len(matrix),len(matrix[0])
        grid = [[[True,1] for _ in range(n)] for _ in range(m)]

        def dfs(ik: int, jk: int):

            if ik-1>=0 and matrix[ik-1][jk]>matrix[ik][jk]:
                if grid[ik-1][jk][0]:
                    grid[ik-1][jk][0] = False
                    dfs(ik-1,jk)
                grid[ik][jk][1] = max(grid[ik][jk][1],1+grid[ik-1][jk][1])
            
            if ik+1<m and matrix[ik+1][jk]>matrix[ik][jk]:
                if grid[ik+1][jk][0]:
                    grid[ik+1][jk][0] = False
                    dfs(ik+1,jk)
                grid[ik][jk][1] = max(grid[ik][jk][1],1+grid[ik+1][jk][1])
            
            if jk-1>=0 and matrix[ik][jk-1]>matrix[ik][jk]:
                if grid[ik][jk-1][0]:
                    grid[ik][jk-1][0] = False
                    dfs(ik,jk-1)
                grid[ik][jk][1] = max(grid[ik][jk][1],1+grid[ik][jk-1][1])
            
            if jk+1<n and matrix[ik][jk+1]>matrix[ik][jk]:
                if grid[ik][jk+1][0]:
                    grid[ik][jk+1][0] = False
                    dfs(ik,jk+1)
                grid[ik][jk][1] = max(grid[ik][jk][1],1+grid[ik][jk+1][1])
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j][0]:
                    grid[i][j][0] = False
                    dfs(i,j)
                    ans = max(ans,grid[i][j][1])
        
        return ans



        