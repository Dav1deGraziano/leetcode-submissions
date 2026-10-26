class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        appeared = []
        res = 0
        crt_len = 0
        for ch in s:
            if ch in appeared:
                res = max(res,crt_len)
                appeared = appeared[appeared.index(ch)+1:]+[ch]
                crt_len = len(appeared)
            else:
                appeared.append(ch)
                crt_len+=1
        
        return max(crt_len,res)

        
        