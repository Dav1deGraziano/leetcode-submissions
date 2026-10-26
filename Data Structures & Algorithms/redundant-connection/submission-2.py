class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def dfs(node: int, visited: Set[int]) -> None:
            for nxt in nei[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt, visited)

        n = len(edges)
        nei = [set() for _ in range(n)]

        for u, v in edges:
            nei[u - 1].add(v - 1)
            nei[v - 1].add(u - 1)

        for u, v in edges[::-1]:
            nei[u - 1].remove(v - 1)
            nei[v - 1].remove(u - 1)

            visited = {0}
            dfs(0, visited)

            if len(visited) == n:
                return [u, v]

            nei[u - 1].add(v - 1)
            nei[v - 1].add(u - 1)