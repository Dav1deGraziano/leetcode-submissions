class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = []
        neg = []
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[2*i+1] = neg[i]
        
        return nums

        