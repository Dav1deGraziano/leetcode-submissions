class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = sorted(zip(capital, profits))
        queue = []
        i = 0
        n = len(projects)

        while i < n and projects[i][0] <= w:
            queue.append(projects[i][1])
            i += 1

        while k > 0 and queue:
            idx = queue.index(max(queue))
            profit = queue.pop(idx)
            w += profit

            while i < n and projects[i][0] <= w:
                queue.append(projects[i][1])
                i += 1

            k -= 1

        return w