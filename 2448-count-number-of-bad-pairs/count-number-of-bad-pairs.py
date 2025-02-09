class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # re arrange it as n[i] - i == n[j] - j to get number of matches
        numsFound = {}
        totalPairs = 0
        for ind in range(len(nums)):
            curValue = nums[ind] - ind
            if curValue not in numsFound:
                numsFound[curValue] = 0

            totalPairs += ind - numsFound[curValue]
            numsFound[curValue] += 1
        
        return totalPairs