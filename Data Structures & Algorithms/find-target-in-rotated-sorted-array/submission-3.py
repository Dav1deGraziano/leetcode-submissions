class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        if n<=3:
            if target in nums:
                return nums.index(target)
            else:
                return -1
        
        i = n//2

        if nums[i]==target:
            return i
        else:
            ## nums[i] is minimum
            if nums[i]<nums[i+1] and nums[i]<nums[i-1]:
                if target<nums[i]:
                    return -1
                else:
                    if target == nums[0]:
                        return 0
                    elif target > nums[0]:
                        res = self.search(nums[1:i],target)
                        if res == -1:
                            return -1
                        else:
                            return 1 + res
                    elif target == nums[-1]:
                        return n-1
                    elif target < nums[-1]:
                        res = self.search(nums[i+1:n-1],target)
                        if res == -1:
                            return -1
                        else:
                            return i+1 + res
                    else:
                        return -1

            ## nums[i] is maximum
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                if target>nums[i]:
                    return -1
                else:
                    if target == nums[0]:
                        return 0
                    elif target > nums[0]:
                        res = self.search(nums[1:i],target)
                        if res == -1:
                            return -1
                        else:
                            return 1 + res
                    elif target == nums[-1]:
                        return n-1
                    elif target < nums[-1]:
                        res = self.search(nums[i+1:n-1],target)
                        if res == -1:
                            return -1
                        else:
                            return i+1 + res
                    else:
                        return -1

            ## nums[i] is a saddle point
            else:
                if target == nums[0]:
                    return 0
                elif target == nums[-1]:
                    return n-1
                else:
                    if nums[0]<nums[-1]:
                        if target<nums[0] or target>nums[-1]:
                            return -1
                        else:
                            if target>nums[i]:
                                res = self.search(nums[i+1:n-1],target)
                                if res == -1:
                                    return -1
                                else:
                                    return i+1 + res
                            else:
                                res = self.search(nums[1:i],target)
                                if res == -1:
                                    return -1
                                else:
                                    return 1 + res
                    else:
                        if target>nums[0] or target<nums[i]:
                            res = self.search(nums[1:i],target)
                            if res == -1:
                                return -1
                            else:
                                return 1 + res
                        elif target<nums[-1] or target>nums[i]:
                            res = self.search(nums[i+1:n-1],target)
                            if res == -1:
                                return -1
                            else:
                                return i+1 + res
                        else:
                            return -1


