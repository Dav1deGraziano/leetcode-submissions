class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    queue=[[i,j]]
                    distances = [0]
                    while queue:
                        a,b=queue[0][0],queue[0][1]
                        dist = distances[0]+1
                        queue.pop(0)
                        distances.pop(0)
                        if a-1>=0 and grid[a-1][b]>0 and grid[a-1][b]>dist:
                            grid[a-1][b]=dist
                            queue.append([a-1,b])
                            distances.append(dist)
                        if a+1<m and grid[a+1][b]>0 and grid[a+1][b]>dist:
                            queue.append([a+1,b])
                            grid[a+1][b]=dist
                            distances.append(dist)
                        if b-1>=0 and grid[a][b-1]>0 and grid[a][b-1]>dist:
                            queue.append([a,b-1])
                            grid[a][b-1]=dist
                            distances.append(dist)
                        if b+1<n and grid[a][b+1]>0 and grid[a][b+1]>dist:
                            queue.append([a,b+1])
                            grid[a][b+1]=dist
                            distances.append(dist)
