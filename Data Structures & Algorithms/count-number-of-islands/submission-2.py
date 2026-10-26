class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        m = len(grid)
        n = len(grid[0])
        to_be_explored = [[ [i,j,True] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if to_be_explored[i][j][2]:
                    to_be_explored[i][j][2] = False
                    if grid[i][j]=="1":
                        counter += 1
                        queue = []
                        if i+1<m and grid[i+1][j]=="1":
                            queue.append([i+1,j])
                            to_be_explored[i+1][j][2] = False
                        elif i+1<m and to_be_explored[i+1][j][2] and grid[i+1][j]=="0":
                            to_be_explored[i+1][j][2] = False
                        if j+1<n and to_be_explored[i][j+1][2] and grid[i][j+1]=="1":
                            queue.append([i,j+1])
                            to_be_explored[i][j+1][2] = False
                        elif j+1<n and grid[i][j+1]=="0":
                            to_be_explored[i][j+1][2] = False
                        while queue:
                            a,b = queue[0][0],queue[0][1]
                            queue.pop(0)
                            if 0<=b-1 and to_be_explored[a][b-1][2] and grid[a][b-1]=="1":
                                queue.append([a,b-1])
                                to_be_explored[a][b-1][2] = False
                            elif 0<=b-1 and to_be_explored[a][b-1][2] and grid[a][b-1]=="0":
                                to_be_explored[a][b-1][2] = False
                            if b+1<n and to_be_explored[a][b+1][2] and grid[a][b+1]=="1":
                                queue.append([a,b+1])
                                to_be_explored[a][b+1][2] = False
                            elif b+1<n and to_be_explored[a][b+1][2] and grid[a][b+1]=="0":
                                to_be_explored[a][b+1][2] = False
                            if 0<=a-1 and to_be_explored[a-1][b][2] and grid[a-1][b]=="1":
                                queue.append([a-1,b])
                                to_be_explored[a-1][b][2] = False
                            elif 0<=a+1 and to_be_explored[a-1][b][2] and grid[a-1][b]=="0":
                                to_be_explored[a-1][b][2] = False
                            if a+1<m and to_be_explored[a+1][b][2] and grid[a+1][b]=="1":
                                queue.append([a+1,b])
                                to_be_explored[a+1][b][2] = False
                            elif a+1<m and to_be_explored[a+1][b][2] and grid[a+1][b]=="0":
                                to_be_explored[a+1][b][2] = False
                
        return counter