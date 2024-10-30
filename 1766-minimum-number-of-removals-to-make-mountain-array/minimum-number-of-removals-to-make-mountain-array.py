class Solution:
    def solve(self, ind, mode, firstCall):
        # returns max number of elements we can keep,when including this index
        if (ind, mode, firstCall) in self.sols:
            return self.sols[(ind, mode, firstCall)]
        if ind == len(self.nums) - 1: 
            return mode == 1 and 1 or -999999

        options = [1]
        for nextInd in range(ind + 1, len(self.nums)):
            if mode == 0 and self.nums[ind] < self.nums[nextInd]:
                options.append(1 + self.solve(nextInd, 0, False))
            elif not firstCall and self.nums[ind] > self.nums[nextInd]:
                options.append(1 + self.solve(nextInd, 1, False))

        best = max(options)
        if mode == 0 and best <= 1: # cant be last element
            best = -999999
        self.sols[(ind, mode, firstCall)] = best
        return best


    def minimumMountainRemovals(self, nums: List[int]) -> int:
        options = [0]
        self.sols = {}
        self.nums = nums

        for ind in range(len(nums)):
            options.append(self.solve(ind, 0, True))

        return len(nums) - max(options)
        