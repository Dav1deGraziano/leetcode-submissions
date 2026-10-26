class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 3):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            b_prev = None
            for j in range(i + 1, n - 2):
                b = nums[j]
                if b == b_prev:
                    continue
                b_prev = b

                crt_target = target - a - b
                k, l = j + 1, n - 1

                while k < l:
                    s = nums[k] + nums[l]

                    if s == crt_target:
                        ans.append([a, b, nums[k], nums[l]])

                        c = nums[k]
                        d = nums[l]

                        k += 1
                        l -= 1

                        # Skip duplicate c/d
                        while k < l and nums[k] == c:
                            k += 1
                        while k < l and nums[l] == d:
                            l -= 1

                    elif s < crt_target:
                        k += 1

                    else:
                        l -= 1

        return ans