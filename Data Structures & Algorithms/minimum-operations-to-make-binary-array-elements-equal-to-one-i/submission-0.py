class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                if i>=n-2:
                    return -1
                ans += 1
                nums[i:i+3] = [1-nums[i+j] for j in range(3)]
        
        return ans
