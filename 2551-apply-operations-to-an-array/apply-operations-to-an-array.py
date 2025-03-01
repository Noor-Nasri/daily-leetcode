class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        count_zero = 0
        for ind in range(len(nums)):
            if nums[ind] == 0:
                count_zero += 1
            elif ind < len(nums) - 1 and nums[ind] == nums[ind + 1]:
                nums[ind + 1] = 0
                result.append(nums[ind] * 2)
            else:
                result.append(nums[ind])
        
        for i in range(count_zero):
            result.append(0)
        
        return result
        