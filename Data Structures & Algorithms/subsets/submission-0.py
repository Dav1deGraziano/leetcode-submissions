class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        elif len(nums)==1:
            return [[],nums]

        res = [[]]
        current_level = [[x] for x in nums]
        res.extend(current_level)
        current_subset_length = 2

        while current_subset_length < len(nums):
            prev_level = [subs for subs in current_level]
            current_level = []
            for subset in prev_level:
                remaining_numbers = [x for x in nums if x not in subset]
                for x in remaining_numbers:
                    dummy = subset+[x]
                    condition = True
                    for new_subset in current_level:
                        if len([x for x in dummy if x not in new_subset])==0:
                            condition = False
                    if condition:
                        current_level.append(dummy)
            res.extend(current_level)
            current_subset_length = current_subset_length + 1

        res.append(nums)
        return res