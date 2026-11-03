class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        n_even = 0
        n_odd = 0
        prefix = 0
        ans = 0

        for i in range(len(arr)):

            prefix += arr[i]
            if prefix % 2 == 1:
                ans += 1+n_even
                n_odd += 1
            else:
                ans += n_odd
                n_even += 1
        
        return ans % (10**9+7)



        