class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        n = len(s)
        dp = [[] for _ in range(n)]
        dp[-1] = [0,1] if s[-1]=='0' else [1,0]

        for i in range(n-2,-1,-1):
            dp[i] = [min(dp[i+1][1],dp[i+1][0]),dp[i+1][1]]
            if s[i]=='0':
                dp[i][1] += 1
            else:
                dp[i][0] += 1
        
        return min(dp[0])
                




