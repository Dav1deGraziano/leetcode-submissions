class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        deck_size = len(hand)
        if deck_size % groupSize != 0:
            return False
        elif groupSize == 1:
            return True
        
        hand.sort()

        while hand:
            crt_number = hand[0]
            hand.pop(0)
            for i in range(1,groupSize):
                if crt_number+i not in hand:
                    return False
                else:
                    hand.pop(hand.index(crt_number+i))

        return True
                    



        

        