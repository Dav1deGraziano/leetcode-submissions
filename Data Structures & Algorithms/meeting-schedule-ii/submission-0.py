"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        n = len(intervals)

        if n<=1:
            return n
        
        intervals.sort(key=lambda x:x.start)
        rooms = [[intervals[0]]]
        n_rooms = 1
        i = 1
        while i<=n-1:
            j = 0
            while j<=n_rooms-1:
                if intervals[i].start>=rooms[j][-1].end:
                    rooms[j].append(intervals[i])
                    break
                j = j+1
            if j==n_rooms:
                rooms.append([intervals[i]])
                n_rooms += 1
            i += 1
            
        return n_rooms
        