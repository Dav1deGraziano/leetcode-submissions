from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def DFS(available,crt):

            if not any(available.values()):
                return crt

            res = []

            for k,v in available.items():
                if available[k]>0:
                    available[k] -= 1
                    nxt = [[int(k)]] if not crt else [x+[int(k)] for x in crt]
                    res.extend(DFS(available,nxt))
                    available[k] += 1
            
            return res
        
        return DFS(Counter(nums),[])
        