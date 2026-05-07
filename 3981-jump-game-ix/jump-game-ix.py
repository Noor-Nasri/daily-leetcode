class Solution:
    # teleport RIGHT to a SMALLER val or teleport LEFT to a larger val
    # I implemented this wrong because I was thinking of going max right then max val
    # But there can be a lot of intermediate hops to move right, ie keep hopping between > and <

    # There is a trick in here that I am missing..
    # So we jump as far right as possible, then go back to the biggest val, then jump even further right
    # The real observation here is: which points become blockades? 

    # We can group all inds with the max val before them.
    # Then when a larger max val shows up, all values between the 2 max vals go there. 
    # If a smaller value shows up, then the previous max val group can jump to the next one!!
    # So just a stack! I did a three sweep + BinarySearch solution when its just stack, LOL

    def maxValue(self, nums: List[int]) -> List[int]:
        previousPeakValues = [] # [[value, rangeStart, rangeEnd]]
        currentMaxValue = nums[0]
        currentRangeStart = 0

        for ind in range(1, len(nums)):
            val = nums[ind]

            if val > currentMaxValue:
                previousPeakValues.append([currentMaxValue, currentRangeStart, ind - 1])
                currentRangeStart, currentMaxValue = ind, val
            
            while previousPeakValues and val < previousPeakValues[-1][0]:
                # Since previous group can jump here, they can now use the new peak
                _, currentRangeStart, _ = previousPeakValues.pop()
        
        previousPeakValues.append([currentMaxValue, currentRangeStart, len(nums) - 1])
        
        finalArr = [-1 for i in range(len(nums))]
        for maxVal, indStart, indEnd in previousPeakValues:
            for ind in range(indStart, indEnd + 1):
                finalArr[ind] = maxVal

        return finalArr
