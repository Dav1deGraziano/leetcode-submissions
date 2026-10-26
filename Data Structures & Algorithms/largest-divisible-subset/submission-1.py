class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = len(nums)
        dp = [(1,set([nums[i]])) for i in range(n)]
        crt_best = 1
        crt_best_idx = n-1

        for i in range(n-2,-1,-1):
            best_idx = None
            num = nums[i]
            for j in range(i+1,n):
                if nums[j]%num==0:
                    if best_idx is None or dp[j][0]>dp[best_idx][0]:
                        best_idx = j
            if best_idx is not None:
                dummy = 1+dp[best_idx][0]
                dp[i] = (dummy,dp[i][1]|dp[best_idx][1])
                if dummy>crt_best:
                    crt_best = dummy
                    crt_best_idx = i

        return list(dp[crt_best_idx][1])


        