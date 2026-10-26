from collections import deque
from typing import List

class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()          # indices with increasing prefix values
        res = n + 1

        for j in range(n + 1):

            while dq and prefix[j] - prefix[dq[0]] >= k:
                res = min(res, j - dq.popleft())

            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
                
            dq.append(j)

        return res if res <= n else -1