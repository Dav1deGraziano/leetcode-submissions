class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for i in range(9):
            appeared = []
            for j in range(9):
                if board[i][j]!=".":
                    if int(board[i][j]) in appeared:
                        return False
                    else:
                        appeared.append(int(board[i][j]))

        # check columns
        for j in range(9):
            appeared = []
            for i in range(9):
                if board[i][j]!=".":
                    if int(board[i][j]) in appeared:
                        return False
                    else:
                        appeared.append(int(board[i][j]))
        
        # check sub-boxes
        for i in range(0,7,3):
            for j in range(0,7,3):
                appeared = []
                for ik in range(3):
                    for jk in range(3):
                        if board[i+ik][j+jk]!=".":
                            if int(board[i+ik][j+jk]) in appeared:
                                return False
                            else:
                                appeared.append(int(board[i+ik][j+jk]))
        
        return True

        