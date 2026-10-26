from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        n = len(asteroids)

        collisions = deque()
        deleted = set()
        found = False

        for i in range(n):

            if not found and asteroids[i]>0:
                found = True
            
            if found and asteroids[i]<0 and asteroids[i-1]>0:
                collisions.append((i-1,i))
        
        while collisions:

            i,j = collisions.pop()
            ast_i = asteroids[i]
            ast_j = -asteroids[j]

            if ast_i<ast_j:
                deleted.add(i)
                while i-1>=0 and i-1 in deleted:
                    i -= 1
                if i-1>=0 and asteroids[i-1]>0:
                    collisions.append((i-1,j))

            elif ast_i>ast_j:
                deleted.add(j)
                while j+1<n and j+1 in deleted:
                    j += 1
                if j+1<n and asteroids[j+1]<0:
                    collisions.append((i,j+1))

            else:
                deleted.add(i)
                deleted.add(j)
                while i-1>=0 and i-1 in deleted:
                    i -= 1
                while j+1<n and j+1 in deleted:
                    j += 1
                if i-1>=0 and j+1<n and asteroids[i-1]>0 and asteroids[j+1]<0:
                    collisions.append((i-1,j+1))
        
        return [asteroids[i] for i in range(n) if i not in deleted]



        