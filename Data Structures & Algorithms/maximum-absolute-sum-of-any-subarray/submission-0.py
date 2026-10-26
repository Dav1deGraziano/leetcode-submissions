class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        s = hi = lo = 0

        for x in nums:
            s += x
            hi = max(hi, s)
            lo = min(lo, s)
            
        return hi - lo
            