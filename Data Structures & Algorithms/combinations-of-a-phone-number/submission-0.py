class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def corresponding_letters(digit: int) -> List[str]:
            
            if digit == 2:
                return ["a","b","c"]
            elif digit == 3:
                return ["d","e","f"]
            elif digit == 4:
                return ["g","h","i"]
            elif digit == 5:
                return ["j","k","l"]
            elif digit == 6:
                return ["m","n","o"]
            elif digit == 7:
                return ["p","q","r","s"]
            elif digit == 8:
                return ["t","u","v"]
            else:
                return ["w","x","y","z"]

        
        if not digits:
            return []

        l = len(digits)
        
        if l == 1:
            return corresponding_letters(int(digits[-1]))
        
        conv = corresponding_letters(int(digits[-1]))
        res = []
        for s in self.letterCombinations(digits[0:-1]):
            for ch in conv:
                res.append(s+ch)

        return res



