from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def DFS(available):

            counter = 0

            for k,v in available.items():
                if available[k]>0:
                    available[k] -= 1
                    counter += 1+DFS(available)
                    available[k] += 1
            
            return counter

        my_dict = Counter(tiles)

        return DFS(my_dict)
