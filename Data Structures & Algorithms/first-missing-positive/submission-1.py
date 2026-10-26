class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        nums = set(x for x in nums if x>0)

        if not nums:
            return 1

        for i in range(1,max_num):
            if i not in nums:
                return i
        
        return max_num+1