class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        def DFS(i: int):
            
            h = 0
            for j in graph[i]:
                graph[i].discard(j)
                graph[j].discard(i)
                h = max(h,DFS(j))
                graph[i].add(j)
                graph[j].add(i)
            
            return 1+h


        n = len(edges)+1
        graph = [set() for _ in range(n)]

        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        crt_min = None
        crt_indices = []

        for i in range(n):
            h = DFS(i)
            if crt_min is None or h<crt_min:
                crt_min = h
                crt_indices = [i]
            elif h == crt_min:
                crt_indices.append(i)
        
        return crt_indices
        

        