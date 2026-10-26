class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        max_l = max_r = 0
        water = 0

        while l < r:
            
            if height[l] < height[r]:
                max_l = max(max_l, height[l])
                water += max_l - height[l]
                l += 1
            else:
                max_r = max(max_r, height[r])
                water += max_r - height[r]
                r -= 1

        return water