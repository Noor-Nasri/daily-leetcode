class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # The number range is just [-k] -> [m + k]. This is 3 * 10^5
        # For each number, we can precompute the # of occurances, as well how many can become this number
        origCounts = {}
        MAX_N = max(nums)
        adjustableCounts = [0 for i in range(MAX_N + k * 2 + 2)]
        for num in nums:
            numInd = num + k
            origCounts[num] = origCounts.get(num, 0) + 1
            adjustableCounts[numInd - k] += 1
            adjustableCounts[numInd] -= 1
            adjustableCounts[numInd + 1] += 1
            adjustableCounts[numInd + k + 1] -= 1
        
        bestFreq = 0
        numReachable = 0
        for numInd in range(len(adjustableCounts)):
            num = numInd - k
            numReachable += adjustableCounts[numInd]
            counts = origCounts.get(num, 0) + min(numOperations, numReachable)
            bestFreq = max(bestFreq, counts)

        return bestFreq