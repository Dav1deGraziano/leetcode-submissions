from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs = sorted(weights[i] + weights[i + 1] for i in range(n - 1))
        m = k - 1
        if m == 0:
            return 0
        return sum(pairs[n - 1 - m:]) - sum(pairs[:m])
        