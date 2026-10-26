class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        ans = 0
        prev_idx = n-1


        for i in range(n):
            if 2*nums[i]>target:
                break
            if i>0 and nums[i]==nums[i-1]:
                ans += 2**(prev_idx-i)
            else:
                crt_target = target-nums[i]
                lower,upper = i,prev_idx
                while lower <= upper:
                    idx = lower + (upper - lower) // 2
                    if nums[idx] <= crt_target:
                        lower = idx + 1
                    else:
                        upper = idx - 1
                prev_idx = upper
                ans += 2**(prev_idx-i)
        
        return ans % (10**9+7)


        