class Solution:

    def longestPalindrome(self, s: str) -> str:

        def check_palindrome(s: str,length: int) -> bool:
            i = 0
            while i<length//2:
                if s[i]!=s[-i-1]:
                    return False
                i = i+1
            return True


        str_len = len(s)

        if str_len == 1:
            return s
        
        
        res = 1
        str_res = s[0]
        i = 0

        while str_len-i>res:
            for j in range(str_len-1,i+res-1,-1):
                if check_palindrome(s[i:j+1],j-i+1):
                    if j-i+1>res:
                        res = j-i+1
                        str_res = s[i:j+1]
                    break
            i = i+1

        return str_res
            
        