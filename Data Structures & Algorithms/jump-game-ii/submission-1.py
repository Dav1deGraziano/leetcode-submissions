class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n==1:
            return 0
        nums[-1]=0
        for i in range(n-2,-1,-1):
            if nums[i]==0:
                nums[i]=n+1
            elif i+nums[i]<n-1:
                nums[i] = 1+min(nums[i+1:i+nums[i]+1])
            else:
                nums[i] = 1+min(nums[i+1:])


        return nums[0]
        