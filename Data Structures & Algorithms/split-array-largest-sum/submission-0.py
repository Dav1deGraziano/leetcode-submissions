class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def can_do(x: int) -> bool:

            i = 0
            n_subarrays = 0
            while i<=n-1:
                crt_sum = nums[i]
                if crt_sum>x:
                    return False
                n_subarrays += 1
                while i+1<=n-1 and crt_sum+nums[i+1]<=x:
                    i += 1
                    crt_sum += nums[i]
                i+=1
            
            return True if n_subarrays<=k else False
        
        n = len(nums)
        lower = 0
        upper = sum(nums)

        if k==1:
            return upper

        while lower<upper:
            mid = lower+int((upper-lower)//2)
            if can_do(mid):
                upper = mid
            else:
                lower = mid+1
        
        return lower

        
