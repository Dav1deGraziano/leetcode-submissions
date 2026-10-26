class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n

        ans = cur = 1
        prev = 0  # 1 = up, -1 = down, 0 = equal

        for i in range(1, n):
            if arr[i] > arr[i-1]:
                sign = 1
            elif arr[i] < arr[i-1]:
                sign = -1
            else:
                sign = 0

            if sign != 0 and sign != prev:
                cur += 1
            else:
                cur = 2 if sign != 0 else 1

            prev = sign
            ans = max(ans, cur)

        return ans