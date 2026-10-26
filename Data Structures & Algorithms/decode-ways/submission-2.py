class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0]=="0":
            return 0
        elif len(s)==1:
            return 1
        elif s[-1]=="0":
            if int(s[-2:])>26:
                return 0
            else:
                dp = [0 for ch in s]
                dp[-1],dp[-2] = -1,1
                prev_was_zero = False
        else:
            dp = [0 for ch in s]
            if s[-2]=="0":
                prev_was_zero = True
                dp[-1] = 1
            else:
                prev_was_zero = False
                if int(s[-2:])>26:
                    dp[-1],dp[-2]=1,1
                else:
                    dp[-1],dp[-2]=1,2
            
        

        for i in range(len(s)-3,-1,-1):
            if s[i]=="0" and prev_was_zero:
                return 0
            elif s[i]=="0":
                prev_was_zero = True
            elif prev_was_zero and int(s[i:i+2])>26:
                return 0
            else:
                if prev_was_zero:
                    prev_was_zero = False
                    dp[i]=dp[i+2]
                else:
                    dp[i]=dp[i+1]
                    if int(s[i:i+2])<=26:
                        dp[i]+=dp[i+2]
        print(dp)
        return dp[0]
        