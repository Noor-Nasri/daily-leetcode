class Solution:
    # For the fun of it, we can do this in O(n) by just counting
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        numSmaller = 0
        numTarget = 0
        for num in nums:
            if num == target:
                numTarget += 1
            elif num < target:
                numSmaller += 1
        
        return [i for i in range(numSmaller, numSmaller + numTarget)]
        