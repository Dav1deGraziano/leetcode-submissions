
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i in res:
                continue
            new_vec = nums[:i]+nums[i+1:]
            if target-nums[i] in new_vec:
                j = new_vec.index(target-nums[i])
                if j>=i:
                    j = j+1
                res = [i,j]
                break
        return res
