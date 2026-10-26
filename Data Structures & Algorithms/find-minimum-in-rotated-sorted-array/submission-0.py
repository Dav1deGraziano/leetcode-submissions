class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n <= 2:
            return min(nums)
        
        i = int(n//2)

        if nums[i]<=nums[i+1] and nums[i]<=nums[i-1]:
            return nums[i]
        elif nums[i]>=nums[i+1] and nums[i]>=nums[i-1]:
            return min(nums[i-1],nums[i+1])
        else:
            if nums[i]<nums[0] and nums[i]<nums[-1]:
                if nums[0]>nums[-1]:
                    return self.findMin(nums[0:i])
                else:
                    return self.findMin(nums[i+1:])
            elif nums[i]>nums[0] and nums[i]>nums[-1]:
                if nums[0]>nums[-1]:
                    return self.findMin(nums[i+1:])
                else:
                    return self.findMin(nums[:i])
            else:
                return min(nums[0],nums[-1])

        
        
