class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for ind in range(len(nums)):
            if sum([int(e) for e in str(nums[ind])]) == ind:
                return ind
        
        return -1