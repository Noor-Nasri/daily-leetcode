class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numOperations = 0
        for num in nums:
            if num % 3:
                numOperations += 1
        return numOperations