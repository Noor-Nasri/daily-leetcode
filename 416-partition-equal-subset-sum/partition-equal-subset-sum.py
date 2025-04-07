class Solution:
    def sumSolve(self, ind, curSum1, curSum2):
        if ind == len(self.nums):
            return curSum1 == curSum2
        
        uid = (ind, curSum1, curSum2)
        if uid in self.sols:
            return self.sols[uid]
        
        val = self.nums[ind]
        possible = self.sumSolve(ind + 1, curSum1 + val, curSum2)
        if not possible:
            possible = self.sumSolve(ind + 1, curSum1, curSum2 + val)

        self.sols[uid] = possible
        return self.sols[uid]

    def canPartition(self, nums: List[int]) -> bool:
        self.sols = {}
        self.nums = nums
        return self.sumSolve(0, 0, 0)
        