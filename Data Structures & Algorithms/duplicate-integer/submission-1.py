class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        res = False
        for i in range(0,len(nums)):
            if nums[i] in seen:
                res = True
                break
            seen.add(nums[i])
        return res