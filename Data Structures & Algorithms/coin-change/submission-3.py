class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount==0:
            return 0

        if amount<0:
            return -1

        if amount in coins:
            return 1

        coins = [x for x in coins if x<amount]
        coins.sort()

        if not coins or amount<0 or amount<min(coins):
            return -1
        
        n = len(coins)
        i = n-1
        res = n*amount
        ok = False

        while i>=0:
            j = int(amount//coins[i])
            while j>=1:
                dummy = self.coinChange(coins[:i],amount-j*coins[i])
                if dummy>=0:
                    if j==amount//coins[i] and i==n-1:
                        return j+dummy
                    ok = True
                    res = min(res,j+dummy)
                    
                j -= 1
            i -= 1
        
        if ok:
            return res
        else:
            return -1

        
