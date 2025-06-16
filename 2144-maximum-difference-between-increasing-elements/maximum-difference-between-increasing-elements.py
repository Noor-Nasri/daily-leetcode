class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxNum = 0
        ans = -1

        for ind in range(len(nums) - 1, -1, -1):
            val = nums[ind]
            if val < maxNum and maxNum - val > ans:
                ans = maxNum - val
            elif val > maxNum:
                maxNum = val

        return ans
        