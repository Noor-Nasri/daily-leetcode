class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind, value in enumerate(nums):
            wanted = target - value

            if wanted in seen: 
                return [seen[wanted], ind]
            seen[value] = ind
        