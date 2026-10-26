from functools import lru_cache
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dp(left, right):
            
            if right - left == 1:
                return 0

            ans = 0
            for k in range(left + 1, right):
                ans = max(
                    ans,
                    nums[left] * nums[k] * nums[right]
                    + dp(left, k)
                    + dp(k, right)
                )
            return ans

        return dp(0, n - 1)