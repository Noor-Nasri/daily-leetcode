class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = 0
        lastVal = 0
        bestSum = 0

        for num in nums:
            if num > lastVal:
                curSum += num
            else: 
                curSum = num
            
            if curSum > bestSum:
                bestSum = curSum
            
            lastVal = num

        return bestSum
        