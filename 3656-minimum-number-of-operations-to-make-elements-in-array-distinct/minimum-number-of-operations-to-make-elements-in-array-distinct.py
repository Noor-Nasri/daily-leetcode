class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numOps = 0
        while len(nums) != len(set(nums)):
            if len(nums) <= 3:
                nums = []
            else:
                nums = nums[3:]
            numOps += 1


        return numOps
        