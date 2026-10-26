class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        a = [0]
        vowels = ["a","e","i","o","u"]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                a.append(a[-1]+1)
            else:
                a.append(a[-1])
        
        ans = []
        for query in queries:
            ans.append(a[query[1]+1]-a[query[0]])
        
        return ans
            