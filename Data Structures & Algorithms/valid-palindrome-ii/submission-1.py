class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)
        skipped_F = None
        skipped_B = None

        for i in range(n//2):

            if skipped_F is None and s[i]!=s[n-1-i]:
                skipped_F = True if s[i+1]==s[n-1-i] else False
                skipped_B = True if s[i] == s[n-2-i] else False
            
            elif skipped_F == True and s[i+1]!=s[n-1-i]:
                skipped_F = False

            elif skipped_B == True and s[i]!=s[n-2-i]:
                skipped_B = False
            
            if skipped_F is not None and not skipped_F and not skipped_B:
                return False
            
        return True
        


        