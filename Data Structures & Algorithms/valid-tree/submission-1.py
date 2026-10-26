class Node:

    def __init__(self, x: int):
        self.val = x
        self.nei = {}

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def cycle_exists(node: Node, parent: Optional[Node], visited: set[int]) -> bool:

            visited.add(node.val)

            for nei in node.nei.values():
                if parent and nei.val == parent.val:
                    continue
                if nei.val in visited:
                    return True
                if cycle_exists(nei, node, visited):
                    return True

            return False


        if n==1 and len(edges)==1:
            return False
        elif n<=2:
            return True

        nodes = {str(i): Node(i) for i in range(n)}
        for i,j in edges:
            nodes[str(i)].nei[str(j)] = nodes[str(j)]
            nodes[str(j)].nei[str(i)] = nodes[str(i)]
        
        queue = ["0"]
        visited = set("0")
        while queue:
            node = queue.pop(0)
            node = nodes[node]
            for key in [key for _,key in enumerate(node.nei) if int(key) not in visited]:
                queue.append(key)
                visited.add(int(key))
        
        if len(visited)<n:
            return False
        
        visited = set()
        if cycle_exists(nodes["0"], None, visited):
            return False
        
        return True
        



        