class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        if sum(cost)>sum(gas):
            return -1

        crt_sum = gas[0]-cost[0]
        if crt_sum>=0:
            total_balance = crt_sum
            k = 0
        else:
            total_balance = 0
            k = 1

        for i in range(1,n):
            crt_sum = gas[i]-cost[i]
            if total_balance+crt_sum<0:
                k = i+1
                total_balance = 0
            else:
                total_balance += crt_sum
        
        return k
        


        
        
        
        