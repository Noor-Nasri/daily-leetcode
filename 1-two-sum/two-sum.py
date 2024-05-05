class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind in range(len(nums)):
            wanted = target - nums[ind]
            if wanted in seen:
                return [seen[wanted], ind]
            
            seen[nums[ind]] = ind
        