class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxSeen = 0
        prevGroup = 0
        curLen = 0
        for num in nums:
            if num == 1:
                curLen += 1
            elif num == 0 and curLen:
                prevGroup = curLen
                curLen = 0
            elif num == 0 and curLen == 0:
                prevGroup = 0
            
            maxSeen = max(maxSeen, prevGroup + curLen)
        
        if maxSeen == len(nums):
            return maxSeen - 1
        return maxSeen