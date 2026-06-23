class Solution:
    def largest(self, arr):
        largest = arr[0]
        for num in arr[1:]:
            if num > largest:
                largest = num
        return largest
