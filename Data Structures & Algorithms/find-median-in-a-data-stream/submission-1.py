class MedianFinder:

    def __init__(self):
        self.queue = []
        self.n = 0
        
    def addNum(self, num: int) -> None:
        low = 0
        up = self.n-1
        while low<=up:
            mid = low + (up-low)//2
            if self.queue[mid]<num:
                low = mid+1
            else:
                up = mid-1

        self.queue = self.queue[:low]+[num]+self.queue[low:]
        self.n += 1
        
    def findMedian(self) -> float:
        print(self.queue)
        if self.n % 2 != 0:
            return self.queue[self.n//2]
        else:
            return (self.queue[self.n//2-1]+self.queue[self.n//2])/2
        
        