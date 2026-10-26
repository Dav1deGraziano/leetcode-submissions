class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def can_reach(heights: List[List[int]], reached: List[List[int]], start: List[int]) -> List[List[int]]:

            if start in reached:
                return reached

            reached.append(start)
            queue = [start]

            while queue:
                i,j = queue[0][0],queue[0][1]
                queue.pop(0)
                if i-1>=0 and [i-1,j] not in reached and heights[i-1][j]>=heights[i][j]:
                    reached.append([i-1,j])
                    queue.append([i-1,j])
                if i+1<m and [i+1,j] not in reached and heights[i+1][j]>=heights[i][j]:
                    reached.append([i+1,j])
                    queue.append([i+1,j])
                if j-1>=0 and [i,j-1] not in reached and heights[i][j-1]>=heights[i][j]:
                    reached.append([i,j-1])
                    queue.append([i,j-1])
                if j+1<n and [i,j+1] not in reached and heights[i][j+1]>=heights[i][j]:
                    reached.append([i,j+1])
                    queue.append([i,j+1])
            return reached
        
        m = len(heights)
        n = len(heights[0])

        if m==1:
            return [[0,j] for j in range(n)]
        elif n==1:
            return [[i,0] for i in range(m)]
        
        reached_pacific = []
        for i in range(m):
            reached_pacific = can_reach(heights,reached_pacific,[i,0])
        for j in range(1,n):
            reached_pacific = can_reach(heights,reached_pacific,[0,j])
        
        reached_atlantic = []
        for i in range(m):
            reached_atlantic = can_reach(heights,reached_atlantic,[i,n-1])
        for j in range(0,n-1):
            reached_atlantic = can_reach(heights,reached_atlantic,[m-1,j])
        
        return [x for x in reached_pacific if x in reached_atlantic]

        