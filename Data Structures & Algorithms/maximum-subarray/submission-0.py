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
                res = max(crt_sum,res)

        return res

        