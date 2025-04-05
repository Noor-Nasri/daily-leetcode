class Solution:
    def solveBadlyCuzWhosWatching(self, nums, ind, curXOR):
        if ind == len(nums):
            self.tot += curXOR
        else:
            self.solveBadlyCuzWhosWatching(nums, ind + 1, curXOR)
            self.solveBadlyCuzWhosWatching(nums, ind + 1, curXOR ^ nums[ind])

    def subsetXORSum(self, nums: List[int]) -> int:
        self.tot = 0
        self.solveBadlyCuzWhosWatching(nums, 0, 0)
        return self.tot