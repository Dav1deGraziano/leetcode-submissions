class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)

        if n <= 3:
            return []

        res = []

        for i1 in range(n-3):
            if i1 > 0 and nums[i1] == nums[i1-1]:
                continue
            crt1 = nums[i1]
            if target>=0 and crt1 > target:
                break

            for i2 in range(i1+1, n-2):
                if i2 > i1+1 and nums[i2] == nums[i2-1]:
                    continue
                crt2 = nums[i2]
                crt_sum = crt1+crt2
                if target>=0 and crt_sum > target:
                    break

                for i3 in range(i2+1, n-1):
                    if i3 > i2+1 and nums[i3] == nums[i3-1]:
                        continue
                    crt3 = nums[i3]
                    crt_sum = crt1+crt2+crt3
                    if target>=0 and crt_sum > target:
                        break

                    for i4 in range(i3+1, n):
                        if i4 > i3+1 and nums[i4] == nums[i4-1]:
                            continue
                        crt4 = nums[i4]

                        if crt_sum + crt4 == target:
                            res.append([crt1, crt2, crt3, crt4])
                        elif target>=0 and crt_sum+crt4 > target:
                            break

        return res