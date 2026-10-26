class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            current = numbers[i]
            numbers[i]=2000
            if target-current in numbers:
                res = [1+i,1+numbers.index(target-current)]
                break
        return res