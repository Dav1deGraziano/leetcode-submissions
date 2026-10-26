class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        awt = 0
        k = 0
        for customer in customers:
            if customer[0]>=k:
                k = customer[0]+customer[1]
                awt += customer[1]/n
            else:
                awt += (k-customer[0]+customer[1])/n
                k += customer[1]
        
        return awt
