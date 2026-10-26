import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ok = True
        s = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(math.ceil(len(s)/2)):
            if s[i]!=s[len(s)-1-i]:
                ok = False
        return ok
        