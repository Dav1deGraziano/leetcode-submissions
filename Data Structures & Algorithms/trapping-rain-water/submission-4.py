class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = [0]*n

        # maximum left containment
        prev_max = 0
        for i in range(n):
            if height[i]<prev_max:
                ans[i] = prev_max-height[i]
            else:
                prev_max = height[i]
        
        # maximum right containment
        prev_max = 0
        for i in range(n-1,-1,-1):
            if height[i]<prev_max:
                ans[i] = min(ans[i],prev_max-height[i])
            else:
                ans[i] = 0
                prev_max = height[i]
        
        return sum(ans)

        