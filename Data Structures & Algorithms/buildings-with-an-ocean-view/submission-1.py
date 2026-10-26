class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        n = len(heights)
        ans = [n-1]
        for i in range(n-2,-1,-1):
            if heights[i]>heights[ans[-1]]:
                ans.append(i)
        
        return ans[::-1]
        