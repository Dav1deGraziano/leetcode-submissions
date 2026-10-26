import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries_sorted = sorted((q, i) for i, q in enumerate(queries))

        res = [-1] * len(queries)
        heap = []
        j = 0

        for q, idx in queries_sorted:
            while j < len(intervals) and intervals[j][0] <= q:
                start, end = intervals[j]
                heapq.heappush(heap, (end - start + 1, end))
                j += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[idx] = heap[0][0]

        return res