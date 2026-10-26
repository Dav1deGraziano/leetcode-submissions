class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        graph_in = [set() for _ in range(n)]

        for u,v in edges:
            graph_in[v].add(u)
        
        return [i for i in range(n) if not graph_in[i]]
        