class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s:
            return True

        min_len = min(len(word) for word in wordDict)
        max_len = max(len(word) for word in wordDict)

        wordDict = set(wordDict)

        memo = {}

        def dp(i):

            if i == len(s):
                return True
                
            if i in memo:
                return memo[i]

            for j in range(i + min_len, min(len(s), i + max_len) + 1):
                if s[i:j] in wordDict and dp(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dp(0)