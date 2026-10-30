from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        edges = defaultdict(int)

        for row in wall:
            crt = 0
            for brick in row[:-1]:   
                crt += brick
                edges[crt] += 1

        best = max(edges.values(), default=0)
        return len(wall) - best