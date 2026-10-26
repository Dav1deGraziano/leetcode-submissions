class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def word_exists(board: List[List[str]], i: int, j: int, m: int, n: int, word: str, avoid: List[List[int]]) -> bool:

            if not word:
                return True


            queue = []
            if i+1<=m-1 and [i+1,j] not in avoid and board[i+1][j]==word[0]:
                queue.append([i+1,j])
            if i-1>=0 and [i-1,j] not in avoid and board[i-1][j]==word[0]:
                queue.append([i-1,j])
            if j+1<=n-1 and [i,j+1] not in avoid and board[i][j+1]==word[0]:
                queue.append([i,j+1])
            if j-1>=0 and [i,j-1] not in avoid and board[i][j-1]==word[0]:
                queue.append([i,j-1])

            if not queue:
                return False
            elif len(word)==1:
                return True
            else:
                for cell in queue:
                    if word_exists(board,cell[0],cell[1],m,n,word[1:],avoid+[[i,j]]):
                        return True
                return False


        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if word_exists(board,i,j,m,n,word[1:],[]):
                        return True
        
        return False
        


        