class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for k in range(1, n):
            a, b, c = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            ugly[k] = min(a, b, c)
            if ugly[k] == a: i2 += 1
            if ugly[k] == b: i3 += 1
            if ugly[k] == c: i5 += 1
        return ugly[-1]