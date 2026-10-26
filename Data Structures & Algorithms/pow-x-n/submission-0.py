class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1.0
        elif x == 0.0:
            return 0.0
        
        if n<0:
            x = 1/x
            n = -n
        
        res = x
        for i in range(2,n+1):
            res *= x
        
        return res
        
        