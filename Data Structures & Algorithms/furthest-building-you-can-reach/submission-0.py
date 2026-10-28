from collections import deque

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        best = 0
        queue = deque([(0,bricks,ladders)])
        n = len(heights)

        while queue:

            i,b,l = queue.pop()

            if i+1<n and heights[i+1]<=heights[i]:
                best = max(best,i+1)
                queue.append((i+1,b,l))
                continue

            if i+1<n:
                if l>0:
                    best = max(best,i+1)
                    queue.append((i+1,b,l-1))
                if heights[i+1]-heights[i]<=b:
                    best = max(best,i+1)
                    queue.append((i+1,b-(heights[i+1]-heights[i]),l))
        
        return best

