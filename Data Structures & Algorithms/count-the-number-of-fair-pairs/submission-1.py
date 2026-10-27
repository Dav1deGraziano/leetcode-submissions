class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n-1):
            
            lo = lower-nums[i]
            hi = upper-nums[i]

            start_lo, end_lo = i+1, n
            start_hi, end_hi = i+1, n

            while start_lo<end_lo or start_hi<end_hi:

                if start_lo<end_lo:

                    idx = (start_lo+end_lo)//2

                    if nums[idx]<lo:
                        start_lo = idx+1
                    else:
                        end_lo = idx
                
                if start_hi<end_hi:

                    idx = (start_hi+end_hi)//2

                    if nums[idx]>hi:
                        end_hi = idx
                    else:
                        start_hi = idx+1
            
            ans += start_hi-start_lo

        return ans