class Solution:
    # So they just gave us the easy again with medium constraints lol
    # Okay, already solved yesterday. 
    # We just track minVals[i] = min(i, .., n) then do one sweep to check each (max - min)
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minFromInd = [nums[-1]]
        for ind in range(len(nums) - 2, -1, -1):
            minFromInd.append(min(nums[ind], minFromInd[-1]))
        
        minFromInd = minFromInd[::-1] 
        maxVal = -1
        for ind in range(len(nums)):
            maxVal = max(maxVal, nums[ind])
            score = maxVal - minFromInd[ind]
            if score <= k:
                return ind

        return -1
        