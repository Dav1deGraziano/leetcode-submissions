class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []
        elif len(nums)==1:
            return [[],nums]
        else:
            nums.sort()
            res = self.subsetsWithDup(nums[1:])
            if nums[0]!=nums[1]:
                for subset in res[1:]:
                    res.append(subset+[nums[0]])
                res.append([nums[0]])
            else:
                i = 1
                final_subset = [nums[0]]
                len_nums = len(nums)-1
                while i<=len_nums:
                    if nums[i]==nums[0]:
                        final_subset.append(nums[0])
                        i = i+1
                    else:
                        break
                for subset in res[1:]:
                    if len(subset)==len_nums:
                        res.append(subset+[nums[0]])
                    elif len([0 for x in subset if x==nums[0]])==i-1:
                        res.append(subset+[nums[0]])
                if i<=len_nums and final_subset not in res:
                    res.append(final_subset) 
            return res
            



        