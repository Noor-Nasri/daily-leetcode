class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxValRemaining = [0 for i in range(len(nums))]
        curMax = 0
        for ind in range(len(nums) - 1, -1, -1):
            curMax = max(curMax, nums[ind])
            maxValRemaining[ind] = curMax
        
        maxVal = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                val = (nums[i] - nums[j]) * maxValRemaining[j + 1]
                maxVal = max(maxVal, val)
        
        return maxVal