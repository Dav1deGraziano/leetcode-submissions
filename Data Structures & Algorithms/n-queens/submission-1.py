class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        cols, diag, anti = set(), set(), set()
        placement = []  

        def dfs(i):

            if i == n:
                res.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in placement])
                return

            for j in range(n):

                if j in cols or (i - j) in diag or (i + j) in anti:
                    continue

                cols.add(j) 
                diag.add(i - j) 
                anti.add(i + j)
                placement.append(j)

                dfs(i + 1)

                placement.pop()

                cols.remove(j) 
                diag.remove(i - j) 
                anti.remove(i + j)

        dfs(0)
        return res