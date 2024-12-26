class Solution:
    def findTarget(self, nums, target, ind, curSum):
        if (ind, curSum) in self.sols:
            return self.sols[(ind, curSum)]

        if ind == len(nums):
            return int(target == curSum)

        if curSum + self.sums[ind] < target:
            sol = 0
        elif curSum - self.sums[ind] > target:
            sol = 0
        else:
            sol = self.findTarget(nums, target, ind + 1, curSum + nums[ind])
            sol += self.findTarget(nums, target, ind + 1, curSum - nums[ind])
            
        self.sols[(ind, curSum)] = sol
        return sol

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.sols = {}
        self.sums = [sum(nums)]
        for ind in range(len(nums)):
            self.sums.append(self.sums[-1] - nums[ind])

        return self.findTarget(nums, target, 0, 0)
        