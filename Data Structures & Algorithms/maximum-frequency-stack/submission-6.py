class FreqStack:

    def __init__(self):
        self.stack = {}
        self.len_stack = 0
        

    def push(self, val: int) -> None:
        self.len_stack += 1
        if val in self.stack:
            self.stack[val].append(self.len_stack)
        else:
            self.stack[val] = [self.len_stack]

    def pop(self) -> int:
        res_idx = None
        res = None
        res_freq = None
        for _,key in enumerate(self.stack):
            freq = len(self.stack[key])
            if res_freq is None or freq>res_freq:
                res = key
                res_freq = freq
                res_idx = self.stack[key][-1]
            elif freq==res_freq and self.stack[key][-1]>res_idx:
                res = key
                res_freq = freq
                res_idx = self.stack[key][-1]
        
        self.stack[res].pop(-1)
        if not self.stack[res]:
            del self.stack[res]
        
        return res


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()