class Solution:
    def totalNQueens(self, n: int) -> int:
        
        res = 0
        cols = set()
        diags = set()
        antidiags = set()

        def backtracking(r: int):

            nonlocal res

            for x in range(n):

                if x in cols or n-r+x in diags or r+x in antidiags:
                    continue
                
                if r+1==n:
                    res += 1
                    return
                
                cols.add(x)
                diags.add(n-r+x)
                antidiags.add(r+x)
                
                backtracking(r+1)

                cols.discard(x)
                diags.discard(n-r+x)
                antidiags.discard(r+x)
        
        backtracking(0)

        return res



