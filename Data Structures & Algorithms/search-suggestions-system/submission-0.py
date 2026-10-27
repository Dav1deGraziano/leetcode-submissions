from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()
        ans = []
        prefix = ''
        start = 0

        for ch in searchWord:
            prefix += ch
            start = bisect_left(products, prefix, start)
            ans.append([p for p in products[start:start+3] if p.startswith(prefix)])
            
        return ans