class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        elif len(nums)==1:
            return [nums]
        else:
            res = []
            len_nums = len(nums)
            i = 1
            while i<=len_nums:
                for permutations in self.permute(nums[1:]):
                    res.append([nums[0]]+permutations)
                nums = nums[1:]+[nums[0]]
                i = i+1        
        return res