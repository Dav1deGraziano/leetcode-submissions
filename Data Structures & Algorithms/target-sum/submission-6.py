class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        m = sum(nums)
        if m<target:
            return 0

        dp = [0 for x in range(-m,m+1)]
        dp[m] = 1
        max_visited = 0

        for num in nums:
            new_dp = [0 for x in range(-m,m+1)]
            for x in [x for x in range(m-max_visited,m+max_visited+1) if dp[x]>0]:
                if num == 0:
                    new_dp[x] = 2*dp[x]
                else:
                    new_dp[x-num] = new_dp[x-num] + dp[x]
                    new_dp[x+num] = new_dp[x+num] + dp[x]
            dp = new_dp
            max_visited += num
        
        return dp[m+target]
