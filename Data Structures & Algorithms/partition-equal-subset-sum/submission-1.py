class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def sum_is_half(subnums: List[int], crt_sum: int, crt_len: int) -> bool:

            if crt_sum == half_sum:
                return True

            for i in range(crt_len):
                crt_sum += subnums[i]
                if crt_sum==half_sum:
                    return True
                elif crt_sum>half_sum:
                    return False
                elif sum_is_half(subnums[1:],crt_sum,crt_len-1):
                    return True
            
            return False

            

            

        tot_sum = sum(nums)

        if tot_sum % 2 != 0:
            return False
        
        half_sum = int(tot_sum//2)
        n = len(nums)

        for i in range(n):
            if sum_is_half(nums[i+1:],nums[i],n-i-1):
                return True

        return False
        