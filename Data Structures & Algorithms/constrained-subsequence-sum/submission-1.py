from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        queue = deque()
        queue.append((nums[-1],n-1))
        best = nums[-1]

        for i in range(n-2,-1,-1):
            crt = max(
                nums[i],
                nums[i]+queue[-1][0],
            )
            while queue and queue[-1][1]-i>=k:
                queue.pop()
            while queue and queue[0][0]<crt:
                queue.popleft()
            queue.appendleft((crt,i))
            best = max(best,crt)
        
        return best
