class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)+1
        totalSum = sum(arr)
        expSum = n * (n + 1) // 2
        return expSum - totalSum