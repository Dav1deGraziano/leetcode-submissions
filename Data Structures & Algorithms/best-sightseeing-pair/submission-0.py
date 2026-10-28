class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        n = len(values)
        best = None
        crt_max_j = values[-1]-(n-1)

        for i in range(n-2,-1,-1):
            crt = values[i]+i+crt_max_j
            if best is None or best<crt:
                best = crt
            crt_max_j = max(crt_max_j,values[i]-i)
        
        return best
