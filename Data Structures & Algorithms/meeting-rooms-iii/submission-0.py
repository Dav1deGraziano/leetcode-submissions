class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        rooms = [[] for _ in range(n)]
        meetings.sort()

        for meeting in meetings:
            room_start,ok = None,False
            for i in range(n):
                if not rooms[i]:
                    rooms[i].append(meeting)
                    ok = True
                    break
                elif rooms[i][-1][1]<=meeting[0]:
                    rooms[i].append(meeting)
                    ok = True
                    break
                elif room_start is None or rooms[room_start][-1][1]>rooms[i][-1][1]:
                    room_start = i
            if not ok:
                rooms[room_start].append(
                    [rooms[room_start][-1][1],rooms[room_start][-1][1]+meeting[1]-meeting[0]]
                )
        
        rooms = [len(room) for room in rooms]
        return rooms.index(max(rooms))