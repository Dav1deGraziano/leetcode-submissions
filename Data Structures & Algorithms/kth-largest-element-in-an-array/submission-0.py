class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k_largest = nums[0:k]
        min_nbr = min(k_largest)
        min_nbr_index = k_largest.index(min_nbr)

        for num in nums[k:]:
            if num>min_nbr:
                k_largest[min_nbr_index] = num
                min_nbr = min(k_largest)
                min_nbr_index = k_largest.index(min_nbr)
        
        return min_nbr