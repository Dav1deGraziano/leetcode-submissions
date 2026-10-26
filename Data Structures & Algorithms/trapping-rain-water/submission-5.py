class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        crt_max_l = 0
        crt_max_r = 0

        for i in range(n):
            
            if height[i]>crt_max_l:
                crt_max_l = height[i]
            elif height[i]<crt_max_l:
                left[i] = crt_max_l-height[i]
            
            if height[n-1-i]>crt_max_r:
                crt_max_r = height[n-1-i]
            elif height[n-1-i]<crt_max_r:
                right[n-1-i] = crt_max_r-height[n-1-i]
        
        return sum(min(left[i],right[i]) for i in range(n))


        