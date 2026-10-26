class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.counter = 0
        self.n_keys = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.counter += 1
            self.cache[key][1] += 1
            self.cache[key][2] = self.counter
            return self.cache[key][0]
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        self.counter += 1
        if key in self.cache:
            self.cache[key] = [value,self.cache[key][1]+1,self.counter]
        elif key not in self.cache and self.n_keys < self.capacity:
            self.n_keys += 1
            self.cache[key] = [value,1,self.counter]
        else:
            to_del = None
            freq = None
            last_use = None
            for _,prev in enumerate(self.cache):
                if freq is None:
                    to_del = prev
                    freq = self.cache[prev][1]
                    last_use = self.cache[prev][2]
                elif self.cache[prev][1]<freq:
                    to_del = prev
                    freq = self.cache[prev][1]
                    last_use = self.cache[prev][2]
                elif self.cache[prev][1]==freq and self.cache[prev][2]<last_use:
                    to_del = prev
                    freq = self.cache[prev][1]
                    last_use = self.cache[prev][2]
            del self.cache[to_del]
            self.cache[key] = [value,1,self.counter]



