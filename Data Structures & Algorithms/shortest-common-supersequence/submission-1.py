class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        
        m, n = len(a), len(b)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if a[i] == b[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        i = j = 0
        ans = []

        while i < m and j < n:
            if a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            elif dp[i + 1][j] >= dp[i][j + 1]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

        ans.extend(a[i:])
        ans.extend(b[j:])

        return "".join(ans)