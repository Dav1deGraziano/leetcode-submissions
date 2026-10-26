class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        i = 0
        j = n-1

        while j-i>0:
            res = max(res,(j-i)*min(heights[i],heights[j]))
            if heights[i]<=heights[j]:
                i += 1
            else:
                j -= 1
        
        return res



        