class Solution:
    def countPairs(self, arr, target):
        l, r = 0, len(arr) - 1
        count = 0

        while l < r:
            s = arr[l] + arr[r]

            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                if arr[l] == arr[r]:
                    n = r - l + 1
                    count += n * (n - 1) // 2
                    break
                else:
                    left_count = 1
                    right_count = 1

                    while l + 1 < r and arr[l] == arr[l + 1]:
                        left_count += 1
                        l += 1

                    while r - 1 > l and arr[r] == arr[r - 1]:
                        right_count += 1
                        r -= 1

                    count += left_count * right_count
                    l += 1
                    r -= 1

        return count