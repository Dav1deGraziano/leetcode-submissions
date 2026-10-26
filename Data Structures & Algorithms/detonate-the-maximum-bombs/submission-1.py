from collections import deque

class Solution:
    def maximumDetonation(self, bombs):

        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            x, y, r = bombs[i]
            for j in range(i + 1, n):
                d = (bombs[j][0] - x) ** 2 + (bombs[j][1] - y) ** 2
                if d <= r ** 2:
                    graph[i].append(j)
                if d <= bombs[j][2] ** 2:
                    graph[j].append(i)

        best = 0
        for i in range(n):
            seen = {i}              
            queue = deque([i])
            while queue:
                b = queue.popleft()
                for nb in graph[b]:
                    if nb not in seen:
                        seen.add(nb)
                        queue.append(nb)
            best = max(best, len(seen))
        return best