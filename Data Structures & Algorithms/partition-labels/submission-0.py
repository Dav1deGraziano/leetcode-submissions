class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        n = len(s)
        dct = {s[i]: i for i in range(n)}

        res = []

        i = 0
        while i<=n-1:
            max_idx = dct[s[i]]
            j = i+1
            while j<=max_idx:
                max_idx = max(max_idx,dct[s[j]])
                j += 1
            res.append(max_idx-i+1)
            i = max_idx+1
        
        return res
