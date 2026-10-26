class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        last = {}
        left = 0
        good = 0
        ans = 0

        for right, x in enumerate(nums):
            if x in last:
                last[x] = right
            else:
                last[x] = right

            if len(last) > k:
                old = min(last.values())
                del last[nums[old]]
                left = old + 1
                good = 0

            if len(last) == k:
                good = min(last.values()) - left + 1
                ans += good

        return ans