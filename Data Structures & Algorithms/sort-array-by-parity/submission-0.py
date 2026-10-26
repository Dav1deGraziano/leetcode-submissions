class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        n = len(nums)
        i = 0
        j = n-1

        while i<j:
            if nums[i] % 2 == 0 and nums[j] % 2 == 1:
                i += 1
                j -= 1
            elif nums[i] % 2 == 1 and nums[j] % 2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            elif nums[i] % 2 == 1 and nums[j] % 2 == 1:
                j -= 1
            else:
                i += 1
        
        return nums
            
        