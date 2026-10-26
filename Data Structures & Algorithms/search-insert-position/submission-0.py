class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        start = 0
        end = n-1

        while start<end:
            idx = (start+end)//2
            if nums[idx]<target:
                start = idx+1
            else:
                end = idx
        
        return start if nums[start]>=target else start+1
