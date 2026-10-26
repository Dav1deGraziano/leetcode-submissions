class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        res = 1
        n = len(nums)
        dp = [1 for i in range(n)]

        for i in range(1,n):
            a = nums[i]
            for j in range(i):
                if a>nums[j] and 1+dp[j]>dp[i]:
                    dp[i] = 1+dp[j]

                


        return max(dp)
        