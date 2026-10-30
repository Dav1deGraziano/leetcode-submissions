from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count = defaultdict(int)
        count[0] = 1          
        prefix = 0
        ans = 0

        for x in nums:
            prefix = (prefix + x) % k
            ans += count[prefix]
            count[prefix] += 1

        return ans