from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            gold = grid[i][j]
            grid[i][j] = 0
            best = 0
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    best = max(best, dfs(x, y))
            grid[i][j] = gold
            return gold + best

        return max(dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] > 0) if any(any(r) for r in grid) else 0