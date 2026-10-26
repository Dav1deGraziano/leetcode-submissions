class Solution:
    def trap(self, height: List[int]) -> int:
    
        n = len(height)
        volumes = [0]*(n-2)

        max_right = max(height[2:]+[0])
        max_left = height[0]
        
        i = 1
        while i<n-1:
            volumes[i-1] = max(0,min(max_left,max_right)-height[i])
            if height[i]>max_left:
                max_left = height[i]
            if height[i]==max_right:
                max_right = max(height[i+2:]+[0])
            i = i+1
        
        return sum(volumes)

            

        