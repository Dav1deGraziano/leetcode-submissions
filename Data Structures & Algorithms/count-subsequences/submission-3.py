from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(None)

        def dfs(i, j):
            
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            ans = dfs(i + 1, j)  # skip s[i]
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)  # use s[i]
            return ans

        return dfs(0, 0)