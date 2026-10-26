class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0]*n
        r = [0]*n

        # maximum left containment
        prev_max = 0
        for i in range(n):
            if height[i]<prev_max:
                l[i] = prev_max-height[i]
            else:
                prev_max = height[i]
        
        # maximum right containment
        prev_max = 0
        for i in range(n-1,-1,-1):
            if height[i]<prev_max:
                r[i] = prev_max-height[i]
            else:
                prev_max = height[i]
        
        return sum([min(l[i],r[i]) for i in range(n)])

        