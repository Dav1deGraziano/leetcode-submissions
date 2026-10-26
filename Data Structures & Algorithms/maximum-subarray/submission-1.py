class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        res = max(nums)

        crt_sum = nums[0]
        i = 0

        while i<n-1:
            if crt_sum<=0:
                i = i+1
                crt_sum = nums[i]
            else:
                i = i+1
                crt_sum += nums[i]
                if crt_sum>res:
                    res = crt_sum

        return res

        