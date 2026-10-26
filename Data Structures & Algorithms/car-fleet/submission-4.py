class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(position)
        fleets = [[position[i],speed[i]] for i in range(n)]
        fleets.sort()
        
        times_to_target = [(target-fleets[i][0])/fleets[i][1] for i in range(n-1,-1,-1)]

        i = 0
        while i<=n-2:
            if times_to_target[i]>=times_to_target[i+1]:
                times_to_target.pop(i+1)
                n -= 1
            else:
                i += 1
                
        return n
                    
                
            



        