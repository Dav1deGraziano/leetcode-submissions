class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [prices[-1],0]

        for i in range(n-2,-1,-1):

            dp = [
                max(prices[i]+dp[1],dp[0]),
                max(dp[1],-prices[i]+dp[0]),
            ]
        
        return dp[1]