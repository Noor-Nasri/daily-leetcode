class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        tot = 0
        for ind in range(1, len(nums)):
            left = nums[:ind]
            right = nums[ind:]
            if abs(sum(left) - sum(right)) % 2 == 0:
                tot += 1

        return tot