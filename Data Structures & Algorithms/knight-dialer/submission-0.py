class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [[[0]*3 for _ in range(4)] for _ in range(n-1)]
        dp.append([[1]*3 for _ in range(4)])

        for i in range(n):
            dp[i][3][0], dp[i][3][2] = None, None

        for i in range(n-2, -1, -1):
            for x in range(4):
                for y in range(3):
                    if x == 3 and (y == 0 or y == 2):
                        continue
                    for delta_x, delta_y in [(2,1),(-2,1),(2,-1),(-2,-1)]:
                        if 0 <= x+delta_x <= 3 and 0 <= y+delta_y <= 2 and dp[i+1][x+delta_x][y+delta_y] is not None:
                            dp[i][x][y] += dp[i+1][x+delta_x][y+delta_y]
                        if 0 <= x+delta_y <= 3 and 0 <= y+delta_x <= 2 and dp[i+1][x+delta_y][y+delta_x] is not None:
                            dp[i][x][y] += dp[i+1][x+delta_y][y+delta_x]
                    dp[i][x][y] %= MOD

        ans = 0
        for x in range(3):
            for y in range(3):
                ans += dp[0][x][y]
        ans += dp[0][3][1]

        return ans % MOD