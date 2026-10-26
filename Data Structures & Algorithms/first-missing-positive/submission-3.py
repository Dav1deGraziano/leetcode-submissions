import heapq

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        h = []
        heapq.heappush(h,0)

        for num in nums:
            if not h:
                heapq.heappush(h,num)
            elif num <= h[0]:
                continue
            elif num == h[0] + 1:
                heapq.heappop(h)
                while h and num == h[0] - 1:
                    num = h[0]
                    heapq.heappop(h)
                heapq.heappush(h,num)
            else:
                heapq.heappush(h,num)
        
        return h[0]+1

            
        