class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        for i in range(n-1):
            if (i == 0 and nums[i]<0) or (i>0 and nums[i]*nums[i-1]>0):
                j = i+1
                while j<n:
                    nums[i],nums[j] = nums[j],nums[i]
                    if nums[i]*nums[j]<0:
                        break
                    j += 1
                        
        
        return nums
        