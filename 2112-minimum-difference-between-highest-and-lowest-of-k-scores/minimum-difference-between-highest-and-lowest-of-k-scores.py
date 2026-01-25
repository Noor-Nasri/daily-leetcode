class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        minDiff = nums[-1]
        for ind in range(k - 1, len(nums)):
            diff = nums[ind] - nums[ind - k + 1]
            minDiff = min(minDiff, diff)

        return minDiff
        