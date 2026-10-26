class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = 0
        stack = []  # [start_index, height], heights strictly increasing

        for i, h in enumerate(heights):
            
            start = i
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                ans = max(ans, height * (i - idx))
                start = idx          
            stack.append([start, h])

        for idx, height in stack:    
            ans = max(ans, height * (len(heights) - idx))
        return ans