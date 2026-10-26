class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [set() for _ in range(n)]

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        ans = 0
        discarded = set()

        for i in range(n):
            if i in discarded:
                continue
            
            if not graph[i]:
                ans += 1
                discarded.add(i)
            else:
                ok = True
                crt = set([i])|graph[i]
                for j in crt:
                    if j == i:
                        continue
                    crt.discard(j)
                    if j in discarded or graph[j]!=crt:
                        ok = False
                        discarded = (discarded|graph[j])|crt
                    crt.add(j)
                    if ok:
                        ans += 1
                        discarded |= crt
        return ans
                    


        