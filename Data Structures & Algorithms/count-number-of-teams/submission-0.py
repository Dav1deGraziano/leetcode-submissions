class Solution:
    def numTeams(self, rating: List[int]) -> int:

        n = len(rating)
        dp = [[0, 0] for _ in range(n)]
        ans = 0

        for i in range(n-2, -1, -1):
            crt_num = rating[i]
            for j in range(i+1, n):
                if rating[j] > crt_num:
                    dp[i][0] += 1
                    ans += dp[j][0]
                elif rating[j] < crt_num:
                    dp[i][1] += 1
                    ans += dp[j][1]

        return ans