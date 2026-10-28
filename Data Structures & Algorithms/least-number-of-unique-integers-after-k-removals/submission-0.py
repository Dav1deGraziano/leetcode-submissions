from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        my_dict = Counter(arr)
        queue = []

        for key,val in my_dict.items():

            heapq.heappush(queue,val)
        
        while k>0:

            if queue and queue[0]<=k:
                num = heapq.heappop(queue)
                k -= num
            
            else:
                break
        
        return len(queue)

        
