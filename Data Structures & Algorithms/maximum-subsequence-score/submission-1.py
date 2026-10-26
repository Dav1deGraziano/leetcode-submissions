import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        n = len(nums1)
        arr = [(nums1[i],nums2[i]) for i in range(n)]
        arr.sort(key=lambda x: x[1],reverse=True)

        queue = [arr[i][0] for i in range(k)]
        heapq.heapify(queue)
        crt_sum = sum(queue)
        best = crt_sum*arr[k-1][1]

        for i in range(k,n):
            prev = heapq.heappop(queue)
            heapq.heappush(queue,arr[i][0])
            crt_sum += arr[i][0]-prev
            best = max(best,crt_sum*arr[i][1])
        
        return best
            


            