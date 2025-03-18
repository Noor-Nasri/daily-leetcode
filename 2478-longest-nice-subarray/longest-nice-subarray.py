class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        s = 0
        e = 0
        cur = 0
        bestLen = 1

        while e < len(nums):
            while (cur & nums[e]) != 0:
                cur ^= nums[s]
                s += 1
            
            cur |= nums[e]
            e += 1
            bestLen = max(bestLen, e - s)
        
        return bestLen
