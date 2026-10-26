class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        i = 0
        n = len(nums)
        while i<=n-2:
            if nums[i]>0 and nums[i+1]>0:
                nums[i+1] = nums[i]*nums[i+1]
                nums.pop(i)
                n -= 1
            else:
                i+=1

        res = max(nums)
        crt_prod = nums[0]
        i = 1

        while i<=n-1:
            if nums[i]==0:
                crt_prod = 1
            else:
                crt_prod *= nums[i]
                if crt_prod>res:
                    res = crt_prod
            i += 1
        
        nums = nums[::-1]
        crt_prod = nums[0]
        i = 1

        while i<=n-1:
            if nums[i]==0:
                crt_prod = 1
            else:
                crt_prod *= nums[i]
                if crt_prod>res:
                    res = crt_prod
            i += 1

        return res
        