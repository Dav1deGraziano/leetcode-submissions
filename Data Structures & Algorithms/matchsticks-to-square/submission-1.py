from functools import lru_cache
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        @lru_cache(None)
        def DFS(i: int, config: tuple):

            if i == n:
                return True       

            for j in range(4):
                if config[j] + matchsticks[i] <= side_len:
                    new_config = list(config)
                    new_config[j] += matchsticks[i]
                    if DFS(i + 1, tuple(sorted(new_config))):
                        return True

            return False

        n = len(matchsticks)
        tot_len = sum(matchsticks)

        if n < 4 or tot_len % 4 != 0:
            return False

        side_len = tot_len // 4

        if max(matchsticks) > side_len:
            return False

        matchsticks.sort(reverse=True)

        return DFS(0, (0, 0, 0, 0))