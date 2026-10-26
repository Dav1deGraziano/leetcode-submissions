class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        if not nums:
            return []
        elif len(nums)==1:
            if nums[0]==target:
                return [target]
            else:
                return []

        res = [[x] for x in nums if x==target]
        current_level = [[x] for x in nums if x<target]

        while current_level:
            prev_level = current_level
            current_level = []
            for sequence in prev_level:
                starting_index = nums.index(sequence[-1])
                for x in nums[starting_index:]:
                    new_sum = sum(sequence)+x
                    if new_sum < target:
                        current_level.append(sequence+[x])
                    elif new_sum == target:
                        res.append(sequence+[x])
        
        return res
        
