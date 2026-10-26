class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if n == 1:
            return nums
        
        fh = self.sortArray(nums[:n//2])
        sh = self.sortArray(nums[n//2:])

        if sh[0]>fh[-1]:
            return fh+sh
        
        if sh[-1]<fh[0]:
            return sh+fh
        
        i,j = 0,0
        i_max = n//2-1
        j_max = n-n//2-1
        for k in range(n):
            if i>i_max:
                nums[k] = sh[j]
                j += 1
            elif j>j_max:
                nums[k] = fh[i]
                i += 1
            elif fh[i]<=sh[j]:
                nums[k] = fh[i]
                i += 1
            else:
                nums[k] = sh[j]
                j += 1
        
        return nums

        