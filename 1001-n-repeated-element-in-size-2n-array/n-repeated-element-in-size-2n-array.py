class Solution:
    # We can obv just do a set and stop the moment we find a duplicate
    # But there is a cool idea here: half the list is the same number, so the most spaced out they are is 2. ie a b a c a d a
    # So we can just check against last 2. Edge case: when just 4, they can be 3 apart: a b c a

    def repeatedNTimes(self, nums: List[int]) -> int:
        if nums[0] == nums[1]:
            return nums[0]
        
        if len(nums) == 4:
            if nums[0] == nums[1] or nums[0] == nums[2] or nums[0] == nums[3]:
                return nums[0]
            elif nums[1] == nums[2] or nums[1] == nums[3]:
                return nums[1]
            else:
                return nums[2]
        
        for ind in range(2, len(nums)):
            if nums[ind] == nums[ind - 1] or nums[ind] == nums[ind - 2]:
                return nums[ind]
        