from collections import deque

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        n = len(colors)
        if k == 1:
            return n
        
        queue = deque()
        
        for i in range(k-1):
            if colors[i]==colors[(i+1)%n]:
                queue.append(i)
        
        ans = 0 if queue else 1

        for i in range(1,n):
            if queue and queue[0]==i-1:
                queue.popleft()
            if colors[(i+k-1)%n]==colors[(i+k-2)%n]:
                queue.append((i+k-2)%n)
            if not queue:
                ans += 1
        
        return ans

