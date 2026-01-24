class Solution:
    # Greedy solution: Pair biggest with smallest and work to the middle

    # Is that too naive? Consider the smallest element x and largest y.
    # We want to pair (x, y), but suppose optimal is (x, a) and (b, y)
    # We then know that x + y <= b + y
    # We also know that a + b <= b + y
    # So we can just switch to (x, y) and (a, b). Meaning greedy is proven.

    def minPairSum(self, nums: List[int]) -> int:
        maxSum = 0
        nums = sorted(nums)
        for ind in range(len(nums) // 2):
            maxSum = max(maxSum, nums[ind] + nums[len(nums) - 1 - ind])
        return maxSum
        