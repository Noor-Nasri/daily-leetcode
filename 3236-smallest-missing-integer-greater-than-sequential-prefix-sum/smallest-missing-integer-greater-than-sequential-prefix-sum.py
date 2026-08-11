class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        totalSum = nums[0]
        for ind in range(1, len(nums)):
            if nums[ind] != nums[ind - 1] + 1:
                break
            
            totalSum += nums[ind]

        existingVals = set(nums)
        while totalSum in existingVals:
            totalSum += 1
        
        return totalSum
        