class Solution:
    def checkValidString(self, s: str) -> bool:

        stack_left = []
        stack_jolly = []
        n = len(s)

        for i in range(n):
            if s[i] == "(":
                stack_left.append(i)
            elif s[i] == "*":
                stack_jolly.append(i)
            else:
                if not stack_left and not stack_jolly:
                    return False
                elif not stack_left:
                    stack_jolly.pop(-1)
                else:
                    stack_left.pop(-1)
        
        while stack_left:
            if not stack_jolly or stack_jolly[-1]<stack_left[-1]:
                return False
            else:
                stack_jolly.pop(-1)
                stack_left.pop(-1)
        
        return True
            

