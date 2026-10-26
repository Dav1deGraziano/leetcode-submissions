class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod_non_zeros = 1
        indices_zeros = []
        for i in range(n):
            if nums[i] == 0:
                indices_zeros.append(i)
            else:
                prod_non_zeros *= nums[i]
        
        if len(indices_zeros)>=2:
            return [0 for i in range(n)]
        elif len(indices_zeros)==1:
            res = [0 for i in range(n)]
            res[indices_zeros[0]] = prod_non_zeros
            return res
        else:
            res = [0 for i in range(n)]
            for i in range(n):
                res[i] = int(prod_non_zeros/nums[i])
            return res