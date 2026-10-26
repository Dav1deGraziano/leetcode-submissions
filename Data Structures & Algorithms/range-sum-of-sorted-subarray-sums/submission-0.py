import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        P = [0]
        for i in range(n):
            P.append(P[-1]+nums[i])
        
        ans = []

        for i in range(1,n+1):
            dum = P[i-1]
            for j in range(i,n+1):
                heapq.heappush(ans,P[j]-dum)

        right -= left
        while left>1:
            left -= 1
            heapq.heappop(ans)

        count = 0
        while right>=0:
            right-=1
            count = (count+heapq.heappop(ans))%1000000007
        
        return count




        