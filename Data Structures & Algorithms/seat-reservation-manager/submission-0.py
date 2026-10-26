import heapq
from collections import deque

class SeatManager:
    def __init__(self, n: int):
        self.available = [i for i in range(1,n+1)]
        self.reserved = set()

    def reserve(self) -> int:
        i = heapq.heappop(self.available)
        self.reserved.add(i)
        return i

    def unreserve(self, seatNumber: int) -> None:
        self.reserved.discard(seatNumber)
        heapq.heappush(self.available,seatNumber)
        
