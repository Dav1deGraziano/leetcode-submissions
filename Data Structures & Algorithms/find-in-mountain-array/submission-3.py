class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find the peak
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # 2. Search ascending portion [0, peak]
        left, right = 0, peak

        while left <= right:
            mid = left + (right - left) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        # 3. Search descending portion [peak + 1, n - 1]
        left, right = peak + 1, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid
            elif value > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1