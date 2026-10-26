class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]):

        def DP(h: int, idx: int) -> int:

            res = 1

            k = idx
            for streak in array[idx:]:
                for j in range(lengths[k]):
                    if streak[j]>h and 1+dp[k][j]>res:
                        res = 1+dp[k][j]
                k += 1
            
            return res


        envelopes.sort()
        n = len(envelopes)
        array = []
        dp = []
        lengths = []
        crt_streak = [envelopes[0][1]]
        prev_w = envelopes[0][0]

        for i in range(1,n):
            if envelopes[i][0]!=prev_w:
                prev_w = envelopes[i][0]
                crt_streak.sort()
                lengths.append(len(crt_streak))
                dp.append([1]*lengths[-1])
                array.append(crt_streak)
                crt_streak = [envelopes[i][1]]
            else:
                crt_streak.append(envelopes[i][1])
        
        crt_streak.sort()
        array.append(crt_streak)
        lengths.append(len(crt_streak))
        dp.append([1]*lengths[-1])

        ans = 1
        for i in range(len(lengths)-2,-1,-1):
            j = 0
            for num in array[i]:
                dp[i][j] = DP(num,i+1)
                ans = max(ans,dp[i][j])
                j += 1
            
        return ans
        
        

            





