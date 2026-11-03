class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        seen = {0: None}
        prefix = 0

        for i,num in enumerate(nums):

            prefix += num

            for s,idx in seen.items():
                
                if (prefix-s)%k==0:

                    if idx is None and i>=1:
                        return True
                    if idx is not None and i-idx>=2:
                        return True
            
            if prefix not in seen:
                seen[prefix] = i
        
        return False
            
        