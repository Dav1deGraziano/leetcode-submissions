class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        k = sum(nums)
        if k == 0 or k == n:
            return 0

        ones = sum(nums[:k])
        best = ones  

        for i in range(1, n):
            ones += nums[(i + k - 1) % n] - nums[i - 1]
            best = max(best, ones)

        return k - best