class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        grid = [[0 for j in range(n)] for i in range(m)]

        if text1[-1] in text2:
            i = 0
            while i<n-1:
                grid[-1][i] = 1
                if text1[-1] not in text2[i+1:]:
                    break
                i = i+1
            if i == n-1:
                grid[-1][-1] = 1

        if text2[-1] in text1:
            i = 0
            while i<m-1:
                grid[i][-1] = 1
                if text2[-1] not in text1[i+1:]:
                    break
                i = i+1
        
        k = n-2
        while k>=0:
            i,j = m-2,k
            while i>=0 and j<=n-2:
                if text1[i]==text2[j]:
                    grid[i][j]=1+grid[i+1][j+1]
                else:
                    grid[i][j]=max([grid[i+1][j],grid[i+1][j+1],grid[i][j+1]])
                i,j = i-1,j+1
            k -= 1
        
        k = m-2
        while k>=0:
            i,j = k,0
            while i>=0 and j<=n-2:
                if text1[i]==text2[j]:
                    grid[i][j]=1+grid[i+1][j+1]
                else:
                    grid[i][j]=max([grid[i+1][j],grid[i+1][j+1],grid[i][j+1]])
                i,j = i-1,j+1
            k -= 1

        return grid[0][0]
        
        

        

        