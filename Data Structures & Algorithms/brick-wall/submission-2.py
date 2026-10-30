class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        n = len(wall)
        for i,row in enumerate(wall):
            for j in range(1,len(row)):
                wall[i][j] += wall[i][j-1]

        CPs = list(set(brick for row in wall for brick in row))
        CPs.sort()

        if len(CPs)==1:
            return n

        my_dict = {CP: i for i,CP in enumerate(CPs)}
        ans = [0 for _ in range(len(CPs))]

        for i,row in enumerate(wall):
            
            crt = 0
            idx = 0
            for brick in row:
                idx_crt = my_dict[brick]
                while idx<idx_crt:
                    ans[idx] += 1
                    idx += 1
                idx += 1
        
        return min(ans[:-1])

        