class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    grid[i][j]=0
                    queue=[[i,j]]
                    minutes = [0]
                    while queue:
                        a,b = queue[0][0],queue[0][1]
                        minute = minutes[0]-1
                        queue.pop(0)
                        minutes.pop(0)
                        if a-1>=0 and (grid[a-1][b]==1 or grid[a-1][b]<minute):
                            grid[a-1][b] = minute
                            queue.append([a-1,b])
                            minutes.append(minute)
                        if a+1<m and (grid[a+1][b]==1 or grid[a+1][b]<minute):
                            grid[a+1][b] = minute
                            queue.append([a+1,b])
                            minutes.append(minute)
                        if b-1>=0 and (grid[a][b-1]==1 or grid[a][b-1]<minute):
                            grid[a][b-1] = minute
                            queue.append([a,b-1])
                            minutes.append(minute)
                        if b+1<n and (grid[a][b+1]==1 or grid[a][b+1]<minute):
                            grid[a][b+1] = minute
                            queue.append([a,b+1])
                            minutes.append(minute)
        
        if any(x>0 for row in grid for x in row):
            return -1

        return -min(min(row) for row in grid)