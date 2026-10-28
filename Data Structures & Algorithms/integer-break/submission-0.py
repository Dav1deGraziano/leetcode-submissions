class Solution:
    def integerBreak(self, n: int) -> int:

        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [1 for _ in range(n)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n):
            best = dp[0]*dp[i-1]
            start,end = 1,i-2
            while start<=end:
                best = max(best,max(start+1,dp[start])*max(end+1,dp[end]))
                start += 1
                end -= 1
            dp[i] = best
        
        return dp[-1]

        