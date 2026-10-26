import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        n = len(nums)
        ans = min(n,1)

        heap_min = []
        heap_max = []

        last_deleted = None

        for i in range(n):

            print(i)

            heapq.heappush(heap_min,(nums[i],i))
            heapq.heappush(heap_max,(-nums[i],i))
            
            while -heap_max[0][0]-heap_min[0][0]>limit:

                if last_deleted is None:
                    last_deleted = 0
                elif last_deleted+1<i:
                    last_deleted += 1

                while heap_max[0][1]<=last_deleted:
                    heapq.heappop(heap_max)
                while heap_min[0][1]<=last_deleted:
                    heapq.heappop(heap_min)
            
            if last_deleted is None:
                ans = max(ans,i+1)
            else:
                ans = max(ans,i-last_deleted)
        
        return ans

