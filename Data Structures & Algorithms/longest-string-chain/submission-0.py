class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def compatible_words(s1: str, s2: str, n1: int) -> bool:

            idx = 0
            while idx<n1-1 and s1[idx]==s2[idx]:
                idx += 1
            
            for i in range(idx,n1-1):
                if s1[i+1]!=s2[i]:
                    return False
            
            return True
        
        dct = {}
        max_len = 0
        for word in words:
            n = len(word)
            if n not in dct:
                max_len = max(max_len,n)
                dct[n] = [[word,1]]
            else:
                dct[n].append([word,1])

        best = 1

        for i in range(max_len-1,-1,-1):
            if i in dct and  i+1 in dct:
                for k,dum in enumerate(dct[i]):
                    word2,crt = dum[0],dum[1] 
                    for word1,nxt in dct[i+1]:
                        if compatible_words(word1,word2,i+1):
                            crt = max(crt,1+nxt)
                    dct[i][k][1] = crt
                    best = max(best,crt)
        
        return best
                    
        

        
        
