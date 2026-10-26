class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n==1:
            return 0
        elif n==2:
            return max(prices[1]-prices[0],0)
        
        profit = [[0,0,0,0] for j in range(n)]
        profit[-1] = [-prices[-1],prices[-1],0,0]

        for i in range(n-2,-1,-1):
            profit[i] = [
                -prices[i]+max(profit[i+1][1],profit[i+1][3]),
                prices[i]+profit[i+1][2],
                max(profit[i+1][0],profit[i+1][2]),
                max(profit[i+1][1],profit[i+1][3])
            ]
            print(profit[i])

        return max(profit[0][0],profit[0][2])
        
