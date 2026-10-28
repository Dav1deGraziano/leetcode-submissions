from collections import deque

class NestedIterator:

    def __init__(self, nestedList: List[NestedInteger]):

        self.stack = deque(reversed(nestedList))
        self.nxt = self.go_to_next
        
    
    @property
    def go_to_next(self):
        
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            nxt = self.stack.pop()
            for x in reversed(nxt.getList()):
                self.stack.append(x)
        
        return False
                

    def next(self) -> int:
        if not self.nxt:
            return None
        ans = self.stack.pop().getInteger()
        self.nxt = self.go_to_next
        return ans
        

    def hasNext(self) -> bool:
        return self.nxt