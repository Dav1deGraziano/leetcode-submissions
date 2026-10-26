class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for digit in digits:
            num += str(digit)
        num = str(int(num)+1)
        num_len = len(num)
        if num_len>len(digits):
            digits.append(0)
        for i in range(num_len):
            digits[i]=int(num[i])
        return digits
        
        
        