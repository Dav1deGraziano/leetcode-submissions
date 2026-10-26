class Solution:
    def rob(self, nums: List[int]) -> int:

        nums_len = len(nums)
        if nums_len==1:
            return nums[0]
        elif nums_len==2:
            return max(nums)
        
        prize = [0 for x in nums]
        prize[-1],prize[-2],prize[-3] = nums[-1],nums[-2],nums[-3]+nums[-1]

        for i in range(4,nums_len+1):
            prize[-i] = nums[-i]+max(prize[-i+2],prize[-i+3])
        
        return max([prize[0],prize[1]])