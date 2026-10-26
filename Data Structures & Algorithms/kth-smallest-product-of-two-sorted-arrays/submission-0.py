class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        def floor_div(a, b):
            return a // b

        def ceil_div(a, b):
            return -((-a) // b)

        def lower_bound(arr, target):
            lo, hi = 0, len(arr)

            while lo < hi:
                mid = (lo + hi) // 2

                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        def upper_bound(arr, target):
            lo, hi = 0, len(arr)

            while lo < hi:
                mid = (lo + hi) // 2

                if arr[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        # Count pairs whose product <= x
        def count_le(x):
            count = 0

            for a in nums1:
                if a > 0:
                    # a * b <= x
                    # b <= floor(x / a)
                    target = floor_div(x, a)
                    count += upper_bound(nums2, target)

                elif a < 0:
                    # a * b <= x
                    # b >= ceil(x / a)
                    target = ceil_div(x, a)
                    count += len(nums2) - lower_bound(nums2, target)

                else:
                    # 0 * b = 0
                    if x >= 0:
                        count += len(nums2)

            return count

        # The minimum/maximum product must occur at one of the corners.
        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ]

        lo = min(candidates)
        hi = max(candidates)

        # Binary search for the smallest x
        # such that at least k products are <= x.
        while lo < hi:
            mid = (lo + hi) // 2

            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo