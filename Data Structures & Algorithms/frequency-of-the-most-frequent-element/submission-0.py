class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)

        best = 0
        idx = 0

        while idx<n:
            start = idx
            while idx+1<n and nums[idx+1]==nums[idx]:
                idx += 1
            left = k
            num = nums[idx]
            while start-1>=0 and left>0:
                if num-nums[start-1]<=left:
                    left -= num-nums[start-1]
                    start -= 1
                else:
                    break
            best = max(best,idx-start+1)
            idx += 1
        
        return best

            
        