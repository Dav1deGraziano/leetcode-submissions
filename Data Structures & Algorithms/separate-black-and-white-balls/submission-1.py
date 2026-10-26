class Solution:
    def minimumSteps(self, s: str) -> int:
        
        idx = 0
        n = len(s)
        ans = 0

        for i in range(n):
            if s[i]=='0':
                if i == idx:
                    idx += 1
                else:
                    ans += i-idx
                    idx += 1
        
        return ans
