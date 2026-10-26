class Node:

    def __init__(self, x: int):
        self.val = x
        self.nei = {}

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nodes = {str(i): Node(i) for i in range(n)}

        for i,j in edges:
            nodes[str(i)].nei[str(j)] = nodes[str(j)]
            nodes[str(j)].nei[str(i)] = nodes[str(i)]
        
        visited = set()
        cmpts = 0
        for _,key in enumerate(nodes):
            if key not in visited:
                cmpts += 1
                visited.add(key)
                queue = [key]
                while queue:
                    s = queue.pop(0)
                    if nodes[s].nei:
                        for key2 in [key for _,key in enumerate(nodes[s].nei) if key not in visited]:
                            queue.append(key2)
                            visited.add(key2)
        
        return cmpts
