class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n = len(arr)
        
        windowSum = 0
        for i in range(k):
            windowSum += arr[i]
            
        maxSum = windowSum
        
        for i in range(k,n):
            windowSum += arr[i]
            windowSum -= arr[i-k]
            
            maxSum = max(maxSum , windowSum)
        return maxSum