class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        idx1,n1 = 0,len(word1)
        idx2,n2 = 0,len(word2)
        ans = ''

        while idx1<n1 and idx2<n2:
            ans += word1[idx1]+word2[idx2]
            idx1 += 1
            idx2 += 1
        
        if idx1<n1:
            return ans+word1[idx1:]
        if idx2<n2:
            return ans+word2[idx2:]
        
        return ans
        