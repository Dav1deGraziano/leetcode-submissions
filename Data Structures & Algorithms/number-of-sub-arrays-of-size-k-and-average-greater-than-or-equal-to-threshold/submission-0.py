class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        n = len(arr)
        avg = sum(arr[:k])/k
        if avg>=threshold:
            ans = 1
        else:
            ans = 0

        for i in range(k,n):
            avg = (avg*k-arr[i-k]+arr[i])/k
            if avg >= threshold:
                ans += 1

        return ans
        