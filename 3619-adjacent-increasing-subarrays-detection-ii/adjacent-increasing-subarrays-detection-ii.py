class Solution:
    # We just need to figure out the num increasing until each ind, and the num increasing from each ind
    # Then we can just do one pass, and figure out biggest k at each ind
    
    def fillInLengthOfIncrSubsequences(self, nums, lenIncrArr, forwardPass):
        lastNum = float('-inf')
        curLen = 0
        numberRange = forwardPass and range(len(nums)) or range(len(nums) -1, -1, -1)
        for ind in numberRange:
            seqContinues = (forwardPass and nums[ind] > lastNum) or (not forwardPass and nums[ind] < lastNum)
            curLen = seqContinues and curLen + 1 or 1
            lenIncrArr[ind] = curLen
            lastNum = nums[ind]


    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        lenIncreaseUntilInd = [1 for i in range(len(nums))]
        lenIncreaseFromInd = [1 for i in range(len(nums))]
        self.fillInLengthOfIncrSubsequences(nums, lenIncreaseUntilInd, True)
        self.fillInLengthOfIncrSubsequences(nums, lenIncreaseFromInd, False)

        maxK = 1
        for cutoffInd in range(len(nums) - 1):
            subarrLen = min(lenIncreaseUntilInd[cutoffInd], lenIncreaseFromInd[cutoffInd + 1])
            maxK = max(maxK, subarrLen)
        
        return maxK
