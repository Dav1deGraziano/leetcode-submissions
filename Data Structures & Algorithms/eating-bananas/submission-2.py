class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def number_of_hours(piles: List[int], k: int) -> int:
            hours = 0
            for i in range(len(piles)):
                if piles[i] % k == 0:
                    hours = hours + piles[i]//k
                else:
                    hours = hours + piles[i]//k + 1
            return hours

        k_min = 1
        k_max = max(piles)
        k = k_min
        while k_min<k_max:
            k = k_min + (k_max-k_min)//2
            hours = number_of_hours(piles,k)
            if hours<=h:
                k_max = k
            else:
                k_min = k+1
        
        return k_min


