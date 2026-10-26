class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [2**31-1] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1)

        return -1 if dp[amount] == 2**31-1 else dp[amount]