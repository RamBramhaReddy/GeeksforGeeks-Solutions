class Solution:
    def maxConsecBits(self, arr):
        if not arr:
            return 0

        max_count = 1
        current = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                current += 1
            else:
                max_count = max(max_count, current)
                current = 1

        return max(max_count, current)