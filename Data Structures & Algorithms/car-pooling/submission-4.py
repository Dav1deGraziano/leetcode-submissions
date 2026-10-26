class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        diff = [0] * 1001

        for n, s, e in trips:
            diff[s] += n
            diff[e] -= n   

        cur = 0

        for d in diff:
            cur += d
            if cur > capacity:
                return False
                
        return True