from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        n = len(grid)
        parent = list(range(4 * n * n))
        count = 4 * n * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            nonlocal count
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                count -= 1

        def idx(i, j, k):
            return (i * n + j) * 4 + k   # k: 0=top, 1=right, 2=bottom, 3=left

        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                if c == ' ':
                    union(idx(i, j, 0), idx(i, j, 1))
                    union(idx(i, j, 1), idx(i, j, 2))
                    union(idx(i, j, 2), idx(i, j, 3))
                elif c == '/':
                    union(idx(i, j, 0), idx(i, j, 3))
                    union(idx(i, j, 1), idx(i, j, 2))
                else:  
                    union(idx(i, j, 0), idx(i, j, 1))
                    union(idx(i, j, 2), idx(i, j, 3))

                # connect to the cell below
                if i + 1 < n:
                    union(idx(i, j, 2), idx(i + 1, j, 0))
                # connect to the cell on the right
                if j + 1 < n:
                    union(idx(i, j, 1), idx(i, j + 1, 3))

        return count