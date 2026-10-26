class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def check_palindrome(s: str, n: int) -> bool:
            
            for i in range(int(n//2)+1):
                if s[i]!=s[n-1-i]:
                    return False

            return True
        
        
        if not s:
            return []

        l = len(s)

        if l==1:
            return [[s]]
        
        res = []
        if check_palindrome(s,l):
            res.append([s])

        i = 0
        while i<l-1:
            if check_palindrome(s[0:i+1],i+1):
                for sub in self.partition(s[i+1:]):
                    res.append([s[0:i+1]]+sub)
            i += 1
        
        return res

        