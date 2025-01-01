class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(e) for e in s]

        maxScore = 0
        ones = sum(nums)
        zeros = 0
        
        for ind in range(len(nums) - 1):
            ones -= nums[ind]
            zeros += 1 - nums[ind]
            maxScore = max(maxScore, zeros + ones)
        
        return maxScore
        