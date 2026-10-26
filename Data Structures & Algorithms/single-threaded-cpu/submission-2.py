import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)
        tasks = sorted((s, d, i) for i, (s, d) in enumerate(tasks))
        idx = 0
        t = 0
        queue = []  
        ans = []

        while queue or idx < n:

            if not queue and t < tasks[idx][0]:
                t = tasks[idx][0]

            while idx < n and tasks[idx][0] <= t:
                heapq.heappush(queue, (tasks[idx][1], tasks[idx][2]))
                idx += 1
                
            duration, i = heapq.heappop(queue)
            ans.append(i)
            t += duration

        return ans