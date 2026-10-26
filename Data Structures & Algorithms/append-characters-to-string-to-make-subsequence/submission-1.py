class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        ns = len(s)
        nt = len(t)
        idx = 0

        for i in range(ns):
            if idx<nt and s[i] == t[idx]:
                idx += 1
        
        return nt-idx
        