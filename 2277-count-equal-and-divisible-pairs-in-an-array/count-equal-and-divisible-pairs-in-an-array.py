class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        numPairs = 0
        for ind1 in range(len(nums)):
            for ind2 in range(ind1 + 1, len(nums)):
                if nums[ind1] == nums[ind2] and (ind1 * ind2) % k == 0:
                    numPairs += 1
        
        return numPairs