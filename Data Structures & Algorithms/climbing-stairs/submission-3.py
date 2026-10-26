class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        elif n==2:
            return 2

        crt = [1,2]

        for i in range(3,n):
            crt = [crt[1],crt[1]+crt[0]]

        return sum(crt)
        