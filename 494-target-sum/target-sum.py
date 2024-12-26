class Solution:
    def findTarget(self, nums, target, ind, curSum):
        if (ind, curSum) in self.sols:
            return self.sols[(ind, curSum)]

        if ind == len(nums):
            return int(target == curSum)
        
        sol = self.findTarget(nums, target, ind + 1, curSum + nums[ind])
        sol += self.findTarget(nums, target, ind + 1, curSum - nums[ind])
        self.sols[(ind, curSum)] = sol
        return sol

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.sols = {}
        return self.findTarget(nums, target, 0, 0)
        