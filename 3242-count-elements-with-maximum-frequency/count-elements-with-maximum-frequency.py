class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = {}
        maxFreq = 0
        numSeen = 0
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > maxFreq:
                maxFreq = counts[n]
                numSeen = 1
            elif counts[n] == maxFreq:
                numSeen += 1
        
        return maxFreq * numSeen
        