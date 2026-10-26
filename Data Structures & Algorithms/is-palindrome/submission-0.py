import math
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ok = True
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        for i in range(math.ceil(len(s)/2)):
            if s[i]!=s[len(s)-1-i]:
                ok = False
        return ok
        