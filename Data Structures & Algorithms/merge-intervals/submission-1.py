class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n_intervals = len(intervals)
        
        if n_intervals==1:
            return intervals

        res = []
        intervals.sort(key=lambda x:x[0])
        i = 0
        while i<=n_intervals-2:
            if intervals[i][1]<intervals[i+1][0]:
                res.append(intervals[i])
            else:
                intervals[i+1] = [intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
            i += 1

        res.append(intervals[-1])

        return res

        
        

        