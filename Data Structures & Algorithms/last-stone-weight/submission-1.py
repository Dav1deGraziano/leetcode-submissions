class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def largest_two_elements(stones: List[int]) -> Tuple[List[int],List[int]]:

            if stones[0]>=stones[1]:
                two_largest = stones[0:2]
            else:
                two_largest = [stones[1],stones[0]]

            remaining = []
            
            crt_min = two_largest[1]
            crt_min_index = 1

            for x in stones[2:]:
                if x>crt_min:
                    remaining.append(two_largest[crt_min_index])
                    two_largest[crt_min_index] = x
                    crt_min = min(two_largest)
                    crt_min_index = two_largest.index(crt_min)
                else:
                    remaining.append(x)

            return two_largest,remaining

        len_stones = len(stones)

        while len_stones>2:
            two_largest,remaining = largest_two_elements(stones)
            print(stones,two_largest,remaining)
            stones = remaining
            len_stones = len_stones - 2
            if two_largest[0]!=two_largest[1]:
                stones.append(abs(two_largest[0]-two_largest[1]))
                len_stones = len_stones+1
        
        if len(stones)==1:
            return stones[0]
        else:
            max_weight = max(stones)
            min_weight = min(stones)
            if max_weight == min_weight:
                return 0
            else:
                return max_weight-min_weight
                

        