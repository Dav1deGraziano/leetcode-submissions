import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        if len(prices)<=1:
            return 0
        for i in range(len(prices)-1):
            profits.append(max(prices[i+1:])-prices[i])
        m = max(profits)
        if m<0:
            return 0
        else:
            return m
        