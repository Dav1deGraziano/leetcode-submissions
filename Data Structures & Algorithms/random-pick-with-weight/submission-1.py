import numpy as np

class Solution:

    def __init__(self, w: List[int]):
        
        n = len(w)
        self.n = n
        self.P = [w[0]]
        for i in range(1,n):
            self.P.append(self.P[-1]+w[i])
        

    def pickIndex(self) -> int:

        num = np.random.randint(1,self.P[-1]+1)
        start = 0
        end = self.n-1

        while start<end:
            idx = (start+end)//2
            if self.P[idx]<num:
                start = idx+1
            else:
                end = idx
        
        return start

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()