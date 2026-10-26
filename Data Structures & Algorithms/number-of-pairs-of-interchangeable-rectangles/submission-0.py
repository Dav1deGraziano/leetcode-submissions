from math import comb

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        my_dict = {}

        for w,h in rectangles:
            if w/h in my_dict:
                my_dict[w/h] += 1
            else:
                my_dict[w/h] = 1
        
        ans = 0
        
        return max(ans,0+sum(comb(v,2) for _,v in my_dict.items() if v>1))
