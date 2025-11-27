class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        bestPrevSums = [0 for i in range(k)]
        curSum = 0
        for ind in range(k - 1):
            curSum += nums[ind]

        bestOverAll = None
        for ind in range(k - 1, len(nums)):
            curSum += nums[ind]
            choice = curSum + bestPrevSums[ind % k]
            if choice > 0: # The next subarray can use us on top of their sum
                bestPrevSums[ind % k] = choice
            else:
                bestPrevSums[ind % k] = 0

            if bestOverAll == None or choice > bestOverAll:
                bestOverAll = choice
            

            curSum -= nums[ind - k + 1]

        return bestOverAll
        