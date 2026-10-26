class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        max_endtime = max(endTime)
        jobs = [[a,b,c] for a,b,c in zip(startTime,endTime,profit)]
        jobs.sort()
        print(jobs)
        n = len(jobs)
        dp = [0]*(max_endtime+1)
        res = 0
        prev = jobs[-1][0]

        for i in range(n-1,-1,-1):
            if jobs[i][0] == prev:
                dp[prev] = max(
                    dp[prev],
                    jobs[i][2] + dp[jobs[i][1]]
                )
                res = max(res,dp[prev])
            else:
                for j in range(jobs[i][0]+1,prev+1):
                    dp[j] = dp[prev]
                dp[jobs[i][0]] = jobs[i][2] + max(dp[jobs[i][1]:])
                res = max(res,dp[jobs[i][0]])
                prev = jobs[i][0]
        
        return res

