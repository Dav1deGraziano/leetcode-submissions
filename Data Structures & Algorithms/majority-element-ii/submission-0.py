from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        dct = defaultdict(int)
        n = len(nums)

        for num in nums:
            dct[num] += 1
        
        return [k for k,v in dct.items() if v>n//3]
        