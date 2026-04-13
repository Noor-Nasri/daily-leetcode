class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        maxDist = max(start, len(nums) - start - 1)
        for offset in range(maxDist):
            if start - offset >= 0 and nums[start - offset] == target:
                return offset
            elif start + offset < len(nums) and nums[start + offset] == target:
                return offset
        
        return maxDist