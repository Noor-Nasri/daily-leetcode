class Solution:
    # Fairly straight forward, get two inds in O(n)
    # Then either: remove all from left, all from right, or from both sides

    def minimumDeletions(self, nums: List[int]) -> int:
        # Too lazy to do a manual sweep, this is fine
        minInd = nums.index(min(nums))
        maxInd = nums.index(max(nums))

        options = [
            max(minInd, maxInd) + 1, # Remove from left
            len(nums) - min(minInd, maxInd), # Remove from right
            (min(minInd, maxInd) + 1) + (len(nums) - max(minInd, maxInd)), # Remove from both
        ]

        return min(options)