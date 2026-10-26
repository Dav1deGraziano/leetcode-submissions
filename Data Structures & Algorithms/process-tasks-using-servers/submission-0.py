import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  
        ans = []
        t = 0

        for i, dur in enumerate(tasks):
            t = max(t, i)

            if not free:
                t = busy[0][0]  
                
            while busy and busy[0][0] <= t:
                ft, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))
            w, idx = heapq.heappop(free)
            ans.append(idx)
            heapq.heappush(busy, (t + dur, w, idx))
        return ans