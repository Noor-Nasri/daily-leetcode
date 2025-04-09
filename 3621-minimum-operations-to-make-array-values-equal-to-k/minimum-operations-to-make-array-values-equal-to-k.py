class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        minVal = min(nums)
        if minVal < k:
            return -1
        
        numOperations = len(nums)
        if minVal == k:
            numOperations -= 1
        
        return numOperations
        