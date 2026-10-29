class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        n = len(nums)
        crt_max = nums[0]
        crt_sum = 0

        for i in range(n):
            crt_sum += nums[i]
            crt_max = max(crt_max,(crt_sum + i)//(i + 1))

        return crt_max