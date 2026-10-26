class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        def return_max(arr: List[str]) -> tuple[str,int]:

            crt_min = arr[0]
            crt_min_idx = 0

            for i in range(1,k):
                if compare_numbers(crt_min,arr[i]):
                    crt_min = arr[i]
                    crt_min_idx = i
            
            return crt_min, crt_min_idx

        def compare_numbers(s1, s2):  
            if len(s1) != len(s2):
                return len(s1) > len(s2)
            return s1 >= s2
        
        arr = nums[:k]
        crt_min,crt_min_idx = return_max(arr)

        for i in range(k,len(nums)):
            if not compare_numbers(crt_min,nums[i]):
                arr.pop(crt_min_idx)
                arr.append(nums[i])
                crt_min,crt_min_idx = return_max(arr)
        
        return crt_min
