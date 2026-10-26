class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area = 1
                    grid[i][j]=0
                    queue = []
                    if i+1<m and grid[i+1][j]==1:
                        queue.append([i+1,j])
                        grid[i+1][j]=0
                        area += 1
                    if j+1<n and grid[i][j+1]==1:
                        queue.append([i,j+1])
                        grid[i][j+1]=0
                        area += 1
                    while queue:
                        a,b = queue[0][0],queue[0][1]
                        queue.pop(0)
                        if a-1>=0 and grid[a-1][b]==1:
                            queue.append([a-1,b])
                            grid[a-1][b]=0
                            area += 1
                        if a+1<m and grid[a+1][b]==1:
                            queue.append([a+1,b])
                            grid[a+1][b]=0
                            area += 1
                        if b-1>=0 and grid[a][b-1]==1:
                            queue.append([a,b-1])
                            grid[a][b-1]=0
                            area += 1
                        if b+1<n and grid[a][b+1]==1:
                            queue.append([a,b+1])
                            grid[a][b+1]=0
                            area += 1
                    max_area = max([area,max_area])

        return max_area