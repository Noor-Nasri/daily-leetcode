class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxValRemaining = [0 for i in range(len(nums))]
        curMax = 0
        for ind in range(len(nums) - 1, -1, -1):
            curMax = max(curMax, nums[ind])
            maxValRemaining[ind] = curMax
        
        maxVal = 0
        maxI = nums[0]
        for j in range(1, len(nums) - 1):
            val = (maxI - nums[j]) * maxValRemaining[j + 1]
            maxI = max(maxI, nums[j])
            maxVal = max(maxVal, val)
        
        return maxVal