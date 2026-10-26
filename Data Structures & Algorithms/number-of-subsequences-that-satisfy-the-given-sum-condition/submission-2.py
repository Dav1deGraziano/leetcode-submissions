class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        ans = 0
        i = 0

        while i<n and 2*nums[i]<=target:
            j = i+1
            while j<n:
                if nums[i]+nums[j]>target:
                    break
                j+=1
            ans = (ans+2**(j-i-1))%(10**9+7)
            i += 1
        
        return ans

        