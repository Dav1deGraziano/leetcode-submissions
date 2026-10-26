class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        start = 0
        end = n-1

        while start<end:

            idx = (start+end)//2

            if nums[idx]<target:
                start = idx+1
            else:
                end = idx
        
        if start==n or nums[start]!=target:
            return [-1,-1]

        while start-1>=0 and nums[start-1]==target:
            start -= 1
        while end+1<n and nums[end+1]==target:
            end += 1
        
        return [start,end]
        
        