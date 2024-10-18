class Solution:
    # constraints are n <= 16, I am tired so I'll just brute force
    def bruteForceSolve(self, currentVal, index):
        if index == len(self.nums):
            return int(currentVal == self.maxVal)
        
        return self.bruteForceSolve(currentVal, index + 1) + self.bruteForceSolve(currentVal | self.nums[index], index + 1)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        self.maxVal = 0
        for num in nums:
            self.maxVal |= num

        return self.bruteForceSolve(0, 0)