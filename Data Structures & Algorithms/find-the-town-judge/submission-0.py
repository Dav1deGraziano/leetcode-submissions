class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        graph_in = [set() for _ in range(n)]
        not_trust = set(i for i in range(n))

        for t in trust:
            not_trust.discard(t[0]-1)
            graph_in[t[1]-1].add(t[0]-1)

        l = len(not_trust)

        if l == 0 or l>=2:
            return -1
        
        judge = list(not_trust)[0]
        if judge not in graph_in[judge] and len(graph_in[judge]) == n-1:
            return judge+1
        return -1
        

        
        
        