class Solution:
    def longestStrChain(self, words):

        dp = {}
        
        for w in sorted(words, key=len):
            dp[w] = 1
            for i in range(len(w)):
                p = w[:i] + w[i+1:]
                if p in dp:
                    dp[w] = max(dp[w], dp[p] + 1)

        return max(dp.values())