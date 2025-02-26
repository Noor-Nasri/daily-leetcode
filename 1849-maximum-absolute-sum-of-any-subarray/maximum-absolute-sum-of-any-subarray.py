class Solution:
    def maxAbsoluteSum(self, nums):
        tot, minSum, maxSum = 0, 0, 0
        for num in nums:
            tot += num
            maxSum = max(maxSum, tot)
            minSum = min(minSum, tot)
        return abs(maxSum - minSum)