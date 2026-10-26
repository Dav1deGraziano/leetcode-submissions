class Solution:

    def solve(self, board: List[List[str]]) -> None:

        def return_island(i: int, j:int) -> set:

            island = {str(i)+"-"+str(j)}
            queue = [[i,j]]

            if i-1>=0 and board[i-1][j]=="O":
                queue.append([i-1,j])
                island.add(str(i-1)+"-"+str(j))

            if i+1<=m-1 and board[i+1][j]=="O":
                queue.append([i+1,j])
                island.add(str(i+1)+"-"+str(j))
                    
            if j+1<=n-1 and board[i][j+1]=="O":
                queue.append([i,j+1])
                island.add(str(i)+"-"+str(j+1))

            if j-1>=0 and board[i][j-1]=="O":
                queue.append([i,j-1])
                island.add(str(i)+"-"+str(j-1))
                    
            len_queue = len(queue)-1
            k = 1

            while k<=len_queue:

                i,j = queue[k][0],queue[k][1]
                k += 1

                if i-1>=0 and board[i-1][j]=="O" and str(i-1)+"-"+str(j) not in island:
                    len_queue += 1
                    queue.append([i-1,j])
                    island.add(str(i-1)+"-"+str(j))

                if i+1<=m-1 and board[i+1][j]=="O" and str(i+1)+"-"+str(j) not in island:
                    len_queue += 1
                    queue.append([i+1,j])
                    island.add(str(i+1)+"-"+str(j))
                        
                if j+1<=n-1 and board[i][j+1]=="O" and str(i)+"-"+str(j+1) not in island:
                    len_queue += 1
                    queue.append([i,j+1])
                    island.add(str(i)+"-"+str(j+1))

                if j-1>=0 and board[i][j-1]=="O" and str(i)+"-"+str(j-1) not in island:
                    len_queue += 1
                    queue.append([i,j-1])
                    island.add(str(i)+"-"+str(j-1))
            
            return island


        m = len(board)
        n = len(board[0])
        islands = set()

        for i in range(m):
            if board[i][0]=="O" and str(i)+"-"+str(0) not in islands:
                islands = islands | return_island(i,0)
            if board[i][n-1]=="O" and str(i)+"-"+str(n-1) not in islands:
                islands = islands | return_island(i,n-1)
        
        for j in range(1,n-1):
            if board[0][j]=="O" and str(0)+"-"+str(j) not in islands:
                islands = islands | return_island(0,j)
            if board[m-1][j]=="O" and str(m-1)+"-"+str(j) not in islands:
                islands = islands | return_island(m-1,j)




        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j]=="O" and str(i)+"-"+str(j) not in islands:
                    board[i][j]="X"


                        


