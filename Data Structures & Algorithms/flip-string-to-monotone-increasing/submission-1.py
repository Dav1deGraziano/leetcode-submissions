class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        n = len(s)
        dp = [0,1] if s[-1]=='0' else [1,0]

        for i in range(n-2,-1,-1):
            dp = [min(dp[1],dp[0]),dp[1]]
            if s[i]=='0':
                dp[1] += 1
            else:
                dp[0] += 1
        
        return min(dp)
                




