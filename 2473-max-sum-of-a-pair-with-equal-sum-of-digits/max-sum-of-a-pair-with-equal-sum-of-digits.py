class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitSums = {}
        maxSum = -1

        for num in nums:
            sum_digits = sum([int(e) for e in str(num)])
            if sum_digits in digitSums:
                maxSum = max(maxSum, digitSums[sum_digits] + num)
                digitSums[sum_digits] = max(num, digitSums[sum_digits])

            else:
                digitSums[sum_digits] = num

        return maxSum
        
        
        