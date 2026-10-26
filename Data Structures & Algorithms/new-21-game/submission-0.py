class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        if n < k:
            return 0.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window = 1.0  

        for i in range(1, n + 1):
            dp[i] = window / maxPts
            if i < k:
                window += dp[i]          
            if 0 <= i - maxPts < k:
                window -= dp[i - maxPts] 

        return sum(dp[k:n + 1])