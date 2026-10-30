class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        for i in range(1,n):
            nums[i] += nums[i-1]

        ans = 0
        for i in range(n):
            prev = 0 if i == 0 else nums[i-1]
            for j in range(i,n):
                if (nums[j]-prev)%k==0:
                    ans += 1
        
        return ans