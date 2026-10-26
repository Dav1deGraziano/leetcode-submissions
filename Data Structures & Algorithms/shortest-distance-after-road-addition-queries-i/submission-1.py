from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        dist = [n - 1 - i for i in range(n)]
        preds = [[] for _ in range(n)]
        for i in range(n - 1):
            preds[i + 1].append(i)

        ans = []
        for u, v in queries:
            preds[v].append(u)
            if dist[v] + 1 < dist[u]:
                dist[u] = dist[v] + 1
                stack = [u]
                while stack:
                    x = stack.pop()
                    for p in preds[x]:
                        if dist[x] + 1 < dist[p]:
                            dist[p] = dist[x] + 1
                            stack.append(p)
            ans.append(dist[0])
        return ans