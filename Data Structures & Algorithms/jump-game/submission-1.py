class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)

        if n==1:
            return True
        elif nums[0]==0:
            return False
        elif n==2:
            return True

        for i in range(min(nums[0],n-1),0,-1):
            if self.canJump(nums[i:]):
                return True

        return False