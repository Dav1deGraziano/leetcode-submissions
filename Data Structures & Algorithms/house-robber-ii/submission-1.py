class Solution:
    def rob(self, nums: List[int]) -> int:

        nums_len = len(nums)
        if nums_len==1:
            return nums[0]
        elif nums_len==2:
            return max(nums)
        
        prize_0 = [0 for x in nums]
        prize_1 = [0 for x in nums]
        prize_0[-1],prize_0[-2],prize_0[-3] = 0,nums[-2],nums[-3]
        prize_1[-1],prize_1[-2],prize_1[-3] = nums[-1],nums[-2],nums[-3]+nums[-1]

        for i in range(4,nums_len+1):
            prize_0[-i] = nums[-i]+max(prize_0[-i+2],prize_0[-i+3])
            prize_1[-i] = nums[-i]+max(prize_1[-i+2],prize_1[-i+3])
        
        return max([max(prize_0),max(prize_1[1:])])