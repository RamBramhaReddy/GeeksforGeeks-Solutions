class Solution:
    def floorSqrt(self, n):
        lo, hi = 1, n
        res = 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid <= n:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res