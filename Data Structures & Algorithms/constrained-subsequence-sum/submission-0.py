from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        dp = [num for num in nums]
        queue = deque()
        queue.append((nums[-1],n-1))
        best = nums[-1]

        for i in range(n-2,-1,-1):
            dp[i] = max(
                dp[i],
                dp[i]+queue[-1][0],
            )
            while queue and queue[-1][1]-i>=k:
                queue.pop()
            while queue and queue[0][0]<dp[i]:
                queue.popleft()
            queue.appendleft((dp[i],i))
            best = max(best,dp[i])
        
        return best
