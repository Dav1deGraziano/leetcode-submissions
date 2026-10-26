class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        if intervals[0][0]>=newInterval[0]:
            if intervals[0][0]>newInterval[1]:
                return [newInterval]+intervals
            else:
                res = [[newInterval[0],max(intervals[0][1],newInterval[1])]]+intervals[1:]
                while res[1:]:
                    if res[0][1]<res[1][0]:
                        return res
                    else:
                        res = [[res[0][0],max(res[1][1],res[0][1])]]+res[2:]
                return res

        else:
            n_intervals = len(intervals)
            idx = n_intervals
            while idx>=0:
                idx -= 1
                if intervals[idx][0]<=newInterval[0]:
                    if intervals[idx][1]<newInterval[0]:
                        res = intervals[0:idx+1] + [newInterval] + intervals[idx+1:]
                        idx += 1
                    else:
                        res = intervals[0:idx]+[[intervals[idx][0],max(newInterval[1],intervals[idx][1])]]+intervals[idx+1:]
                    break
            
            while res[idx+1:]:
                if res[idx][1]<res[idx+1][0]:
                    return res
                else:
                    res = res[:idx]+[[res[idx][0],max(res[idx+1][1],res[idx][1])]]+res[idx+2:]
            return res
        
        

        