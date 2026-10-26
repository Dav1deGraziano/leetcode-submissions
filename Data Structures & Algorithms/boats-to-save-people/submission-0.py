class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        dct = {}
        for person in people:
            if str(person) not in dct:
                dct[str(person)] = 1
            else:
                dct[str(person)] += 1
        
        n_boats = 0

        while dct:
            for idx,key in enumerate(dct):
                if idx>=1:
                    break
                key1 = key
            if dct[key1] == 1:
                del dct[key1]
            else:
                dct[key1] -= 1
            n_boats += 1
            for j in range(limit-int(key1),0,-1):
                if str(j) in dct:
                    if dct[str(j)] == 1:
                        del dct[str(j)]
                    else:
                        dct[str(j)] -= 1
                    break

        return n_boats
