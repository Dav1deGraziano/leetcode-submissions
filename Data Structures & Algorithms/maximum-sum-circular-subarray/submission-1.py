class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        ans = []
        n = len(nums)
        i = 0

        while i<n:
            if nums[i]>0:
                crt_sum = nums[i]
                ans.append(crt_sum)
                ok = True
                j = 1
                while i+j<n+i:
                    crt_sum += nums[(i+j)%n]
                    ans[-1] = max(ans[-1],crt_sum)
                    if ok and nums[(i+j)%n]<0:
                        ok = False
                        k = j+1
                    j += 1
                if ok:
                    break
                i += k
            else:
                i += 1

        return max(ans) if ans else max(nums)
        