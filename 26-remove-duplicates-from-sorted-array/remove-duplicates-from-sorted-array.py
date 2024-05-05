class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numDupes = 0
        lastNum = None
        for ind, val in enumerate(nums):
            if val == lastNum:
                numDupes += 1
            else:
                nums[ind - numDupes] = val
                lastNum = val
        return len(nums) - numDupes
        