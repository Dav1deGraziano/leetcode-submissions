import heapq

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        n = len(prices)
        best = [prices[0],prices[1]] if prices[0]<=prices[1] else [prices[1],prices[0]]

        for i in range(2,n):
            if prices[i]<best[1]:
                if prices[i]<best[0]:
                    best = [prices[i],best[0]]
                else:
                    best[1] = prices[i]

        ans = money-best[0]-best[1]
        return ans if ans>=0 else money

        