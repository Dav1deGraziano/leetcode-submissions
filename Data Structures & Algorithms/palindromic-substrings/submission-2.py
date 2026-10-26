class Solution:
    def countSubstrings(self, s: str) -> int:

        def check_palindrome(s: str,length:int) -> bool:

            i = 0
            while i<length//2:
                if s[i]!=s[-i-1]:
                    return False
                i = i+1
            return True

        len_str = len(s)

        if len_str == 1:
            return 1
        elif len_str == 2 and s[0]==s[1]:
            return 3
            
        counter = len_str

        for i in range(0,len_str-1):
            for j in range(i+1,len_str):
                if check_palindrome(s[i:j+1],j-i+1):
                    counter += 1

        return counter
        

        