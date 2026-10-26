class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    counter += 1
                    grid[i][j]="0"
                    queue = []
                    if i+1<m and grid[i+1][j]=="1":
                        queue.append([i+1,j])
                        grid[i+1][j]="0"
                    if j+1<n and grid[i][j+1]=="1":
                            queue.append([i,j+1])
                            grid[i][j+1]="0"
                    while queue:
                        a,b = queue[0][0],queue[0][1]
                        queue.pop(0)
                        if 0<=b-1 and grid[a][b-1]=="1":
                            queue.append([a,b-1])
                            grid[a][b-1]="0"
                        if b+1<n and grid[a][b+1]=="1":
                            queue.append([a,b+1])
                            grid[a][b+1]="0"
                        if 0<=a-1 and grid[a-1][b]=="1":
                            queue.append([a-1,b])
                            grid[a-1][b]="0"
                        if a+1<m and grid[a+1][b]=="1":
                            queue.append([a+1,b])
                            grid[a+1][b]="0"
                
        return counter