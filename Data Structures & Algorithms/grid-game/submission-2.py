class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        top = sum(grid[0])   
        bottom = 0           
        ans = float('inf')

        for k in range(len(grid[0])):
            top -= grid[0][k]
            ans = min(ans, max(top, bottom))
            bottom += grid[1][k]

        return ans