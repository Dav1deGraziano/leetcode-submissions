class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            t = list(t)
            s = list(s)
            for i in range(len(s)):
                if s[i] not in t:
                    return False
                else:
                    t.remove(s[i])

        return True