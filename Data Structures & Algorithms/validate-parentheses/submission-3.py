class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2!=0:
            return False
        for char in s:
            if char in ["(","[","{"]:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if top=="(":
                    if char==")":
                        continue
                    else:
                        return False
                elif top=="[":
                    if char=="]":
                        continue
                    else:
                        return False
                else:
                    if char=="}":
                        continue
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
                    
                