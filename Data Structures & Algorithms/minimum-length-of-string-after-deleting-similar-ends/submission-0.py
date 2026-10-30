class Solution:
    def minimumLength(self, s: str) -> int:
        
        n = len(s)
        start,end = 0,n-1

        while start<end:
            if s[start]!=s[end]:
                break
            while start+1<=end and s[start+1]==s[start]:
                start += 1
            while end-1>=start and s[end-1]==s[end]:
                end -= 1
            start += 1
            end -= 1
        
        return max(0,end-start+1)
