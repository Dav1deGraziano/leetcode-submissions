from collections import deque

class Solution:
    def isBipartite(self, graph):

        color = {}
        for start in range(len(graph)):
            
            if start in color:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
        return True