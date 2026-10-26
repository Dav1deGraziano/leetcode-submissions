class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def check_if_permutation(s1: str, s2: str) -> bool:
            s = {}
            for ch in s2:
                if ch in s:
                    s[ch] += 1
                else:
                    s[ch] = 1

            for ch in s1:
                if ch not in s:
                    return False
                else:
                    if s[ch] >= 2:
                        s[ch] -= 1
                    else:
                        del s[ch]
            return True
                        

        n1 = len(s1)
        n2 = len(s2)
        if n1>n2:
            return False
        
        i = 0

        while i<=n2-n1:
            if check_if_permutation(s1,s2[i:i+n1]):
                return True
            i += 1
        
        return False
            
    
        