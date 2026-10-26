class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [1]*n
        answer[-1] = 0

        i = 0
        while i<=n-3:
            if heights[i]>heights[i+1]:
                counter = 1
                h = heights[i]
                max_in_between = heights[i+1]
                for j in range(i+2,n):
                    if heights[j]>max_in_between:
                        counter+=1
                    if heights[j]>h:
                        break
                    max_in_between = max(max_in_between,heights[j])
                answer[i] = counter
            i += 1
        
        return answer


        