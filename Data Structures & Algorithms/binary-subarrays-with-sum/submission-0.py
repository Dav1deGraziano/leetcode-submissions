class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)
        start = 0
        ans = 0

        if goal == 0:
            for end in range(n):
                if nums[end] == 0:
                    ans += end - start + 1
                else:
                    start = end + 1
            return ans

        crt_sum = 0
        lead = 0  

        for end in range(n):

            crt_sum += nums[end]

            while crt_sum > goal:      
                crt_sum -= nums[start]
                start += 1
                lead = 0

            while crt_sum == goal and nums[start] == 0:   
                start += 1
                lead += 1

            if crt_sum == goal:
                ans += lead + 1
                
        return ans