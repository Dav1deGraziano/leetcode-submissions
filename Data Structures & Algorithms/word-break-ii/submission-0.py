class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict = set(word for word in wordDict)
        n = len(s)
        res = []

        def backtracking(k: int, crt_str: str):

            nonlocal res
            nonlocal n
            nonlocal s
            nonlocal wordDict

            if k==n:
                res.append(crt_str)
                return
            
            for x in range(k,n):
                
                if s[k:x+1] in wordDict:
                    if not crt_str:
                        backtracking(x+1,s[k:x+1])
                    else:
                        backtracking(x+1,crt_str + " " + s[k:x+1])
            
        backtracking(0,"")

        return res
            



        