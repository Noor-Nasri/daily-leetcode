class Solution:
    # In other words, I can decrement one element of the array each move.
    # Then it becomes kind of trivial: just pick smallest, decrement all to it

    def minMoves(self, nums: list[int]) -> int:
        minVal = min(nums)
        return sum(nums) - minVal*len(nums)    