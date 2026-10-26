class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):

            window_max = arr[i]
            crt_max = arr[i]+dp[i+1]

            counter = 2
            while i+counter-1<min(n,i+k):
                if arr[i+counter-1]>window_max:
                    window_max = arr[i+counter-1]
                dum = window_max*(counter)+dp[i+counter]
                if dum>crt_max:
                    crt_max = dum
                counter += 1
            dp[i] = crt_max
        
        return dp[0]



