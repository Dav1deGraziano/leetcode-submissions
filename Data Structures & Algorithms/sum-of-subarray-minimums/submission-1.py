class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        ans = 0
        n = len(arr)

        left = [-1]*n   
        right = [n]*n   
        queue = []

        for i in range(n):
            while queue and arr[queue[-1]] > arr[i]:
                right[queue.pop()] = i
            left[i] = queue[-1] if queue else -1
            queue.append(i)

        for i in range(n):
            ans += arr[i]*(i-left[i])*(right[i]-i)

        return ans % 1000000007