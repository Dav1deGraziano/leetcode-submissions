class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        if not s:
            return len(t)

        idx = 0
        nt = len(t)

        for ch in s:
            if idx < nt and ch == t[idx]:
                idx += 1
        
        return nt-idx
        