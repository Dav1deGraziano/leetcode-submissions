class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pos,neg = [],[]

        for i in range(n):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        
        for i in range(n//2):
            nums[2*i],nums[2*i+1] = pos[i],neg[i]
                        
        
        return nums
        