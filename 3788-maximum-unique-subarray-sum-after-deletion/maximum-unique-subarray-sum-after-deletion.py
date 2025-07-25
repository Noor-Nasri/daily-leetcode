class Solution:
    def maxSum(self, nums: List[int]) -> int:
        elements = {e for e in nums if e > 0}
        if not elements:
            return max(nums)

        return sum(elements)