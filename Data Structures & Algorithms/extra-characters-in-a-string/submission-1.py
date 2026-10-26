class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        new = {}
        for word in dictionary:
            prfx = word[0]
            sufx = word[1:] if len(word)>1 else ''
            if prfx not in new:
                new[prfx] = {sufx: len(sufx)}
            elif sufx not in new[prfx]:
                new[prfx][sufx] = len(sufx)
        
        n = len(s)
        dp = [0 for _ in range(n+1)]

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]              # skip s[i]
            for suffix, lth in new.get(s[i], {}).items():
                if i + lth < n and s[i+1:i+1+lth] == suffix:
                    dp[i] = min(dp[i], dp[i + lth + 1])
        
        print(dp)
        return dp[0]

            
