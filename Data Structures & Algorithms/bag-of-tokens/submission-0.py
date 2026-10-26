class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        score = 0
        tokens.sort()

        n = len(tokens)
        start,end = 0,n-1
        best = 0

        while start<=end:
            if power>=tokens[start]:
                power -= tokens[start]
                start += 1
                score += 1
                best = max(best,score)
            elif score>0:
                power += tokens[end]
                score -= 1
                end -= 1
            else:
                break
        
        return best
