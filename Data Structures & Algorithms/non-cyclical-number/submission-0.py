class Solution:
    def isHappy(self, n: int) -> bool:

        history = [n]

        while 0<=1:
            num = str(history[-1])
            history.append(0)
            for x in num:
                history[-1] += int(x)**2
            if history[-1]==1:
                return True
            elif history[-1] in history[:-1]:
                return False
            
        