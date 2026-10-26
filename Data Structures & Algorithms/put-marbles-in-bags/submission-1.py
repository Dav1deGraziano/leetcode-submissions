class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        if k == 1:
            return 0

        cuts = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        return sum(cuts[-(k - 1):]) - sum(cuts[:k - 1])