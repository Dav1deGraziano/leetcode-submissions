class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        if n==1:
            return 0

        intervals.sort()
        res = [intervals[0]]
        i = 1
        while i<=n-1:
            if res[-1][1]<=intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1]=min(res[-1][1],intervals[i][1])
            i += 1

        return n - len(res)
