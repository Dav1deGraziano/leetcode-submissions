class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        i = 0
        n = len(nums)

        while i+k<=n:
            
            res.append(max(nums[i:i+k]))
            i += 1

        return res
        