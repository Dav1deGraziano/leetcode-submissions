class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count(prefix):
            curr = prefix
            nxt = prefix + 1
            cnt = 0
            while curr <= n:
                cnt += min(n + 1, nxt) - curr
                curr *= 10
                nxt *= 10
            return cnt

        curr = 1
        k -= 1

        while k > 0:
            steps = count(curr)
            if steps <= k:
                curr += 1      # Skip this whole subtree
                k -= steps
            else:
                curr *= 10      # Go into the subtree
                k -= 1

        return curr