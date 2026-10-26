import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = []
        explored = []
        for i in range(len(nums)):
            if nums[i] in explored:
                continue
            else: 
                dummy = 0
                for j in range(i,len(nums)):
                    if nums[j]==nums[i]:
                        dummy = dummy+1
                counter.append(dummy)
                explored.append(nums[i])
        res = []
        while len(counter)>=1:
            i = counter.index(max(counter))
            if explored[i] in res:
                counter = counter[:i]+counter[i+1:]
                explored = explored[:i]+explored[i+1:]
                continue
            res.append(explored[i])
            counter = counter[:i]+counter[i+1:]
            explored = explored[:i]+explored[i+1:]
            print(res)
        return res[:k]

        