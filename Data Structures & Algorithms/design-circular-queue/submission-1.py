class ListNode:

    def __init__(self,val=0,nxt=None,prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = None
        self.n = 0
        self.k = k

    def enQueue(self, value: int) -> bool:

        if self.n == self.k:
            return False

        if self.queue is None:
            self.queue = ListNode(value)
            self.queue.next = self.queue
            self.queue.prev = self.queue

        else:
            self.queue.prev.next = ListNode(value)
            self.queue.prev = self.queue.prev.next

        self.n += 1
        return True
            
        
    def deQueue(self) -> bool:

        if self.queue is None:
            return False
        
        elif self.n == 1:
            self.queue = None
        
        else:
            self.queue.prev.next,self.queue.next.prev = self.queue.next,self.queue.prev
            self.queue = self.queue.next

        self.n -= 1
        return True

        

    def Front(self) -> int:
        return -1 if self.queue is None else self.queue.val
        

    def Rear(self) -> int:
        return -1 if self.queue is None else self.queue.prev.val
        
    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()