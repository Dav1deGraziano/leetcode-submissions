class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:

        self.nums.append(val)
        nums = self.nums
        k = self.k

        k_largest = nums[0:k]
        current_min = min(k_largest)
        index_crt_min = k_largest.index(current_min)

        for x in nums[k:]:
            if x>current_min:
                k_largest[index_crt_min] = x
                current_min = min(k_largest)
                index_crt_min = k_largest.index(current_min)
        
        return min(k_largest)
