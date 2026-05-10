class Solution:
    # So at any point, you can jump forward to any ind with value within target away
    # Since you only go forward, this is clearly DP
    # [ind] -> max # of jumps or -1
    
    # We can optimize the options at each ind by pre-solving jump abilities by sorting
    # But this will still be n^2 because all numbers can be within target
    # So I'll just make the whole solution n^2 and iterate on all vals after ind. Lol.

    def maxJumpsFromInd(self, sols, nums, maxDiff, ind):
        if ind in sols:
            return sols[ind]
        elif ind == len(nums) - 1:
            return 0

        val = nums[ind]
        bestOption = -1
        for nextInd in range(ind + 1, len(nums)):
            if abs(nums[nextInd] - val) <= maxDiff:
                option = self.maxJumpsFromInd(sols, nums, maxDiff, nextInd)
                if option != -1 and option >= bestOption:
                    bestOption = option + 1
                

        sols[ind] = bestOption
        return sols[ind]
        
    def maximumJumps(self, nums: List[int], target: int) -> int:
        return self.maxJumpsFromInd({}, nums, target, 0)