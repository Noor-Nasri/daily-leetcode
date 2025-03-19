class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for ind in range(len(nums) - 2):
            if nums[ind] == 0:
                operations += 1
                for bonus in range(3):
                    nums[ind + bonus] = 1 - nums[ind + bonus]
        
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        
        return operations
            
        