class Solution:
    def maxWater(self, arr):
        maxarea = 0
        l, r = 0, len(arr) - 1

        while l < r:
            w = r - l
            h = min(arr[l], arr[r])
            maxarea = max(maxarea, h * w)

            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1

        return maxarea