class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def bin_search(i: int, j: int):

            while i<j:
                idx = (i+j)//2
                if nums[idx]<target:
                    i = idx+1
                else:
                    j = idx
            
            return True if nums[i]==target else False
        
        n = len(nums)
        crt_min = None
        crt_min_idx = None
        for i in range(n):
            if crt_min is None or nums[i]<=crt_min:
                crt_min = nums[i]
                crt_min_idx = i
        while crt_min_idx-1>=0 and nums[crt_min_idx-1]==crt_min:
            crt_min_idx -= 1

        
        if target==nums[0]:
            return True
        elif target<nums[0]:
            return bin_search(crt_min_idx,n-1)
        else:
            if crt_min_idx == 0:
                crt_min_idx = n-1
            return bin_search(0,crt_min_idx)
        

        