class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost)==1:
            return cost[0]
        elif len(cost)==2:
            return min(cost)
        
        dp = [0 for x in cost]
        dp[-1],dp[-2] = cost[-1],cost[-2]

        for i in range(3,len(cost)+1):
            dp[-i] = cost[-i]+min(dp[-i+1],dp[-i+2])
        
        return min(dp[0],dp[1])