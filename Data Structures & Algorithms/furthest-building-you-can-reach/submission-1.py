import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        best = 0
        queue = []
        n = len(heights)

        for i in range(n - 1):

            climb = heights[i+1] - heights[i]

            if climb > 0:
                heapq.heappush(queue, climb)

                if len(queue) > ladders:
                    bricks -= heapq.heappop(queue)  

                if bricks < 0:
                    break

            best = i + 1

        return best