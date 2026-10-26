class Solution:
    def countSubstrings(self, s: str) -> int:

        def check_palindrome(s: str,length:int) -> bool:

            i = 0
            while i<=length//2:
                if s[i]!=s[-i-1]:
                    return False
                i = i+1
            return True

        len_str = len(s)-1

        if len_str == 0:
            return 1
        elif len_str == 1 and s[0]==s[1]:
            return 3
            
        counter = len_str+1

        for i in range(0,len_str):
            for j in range(i+1,len_str+1,2):
                if check_palindrome(s[i:j+1],j-i+1):
                    counter += 1
            if i>=1:
                for j in range(min([i,len_str-i]),0,-1):
                    if check_palindrome(s[i-j:i+j+1],2*j+1):
                        counter += j
                        break

        return counter
        

        