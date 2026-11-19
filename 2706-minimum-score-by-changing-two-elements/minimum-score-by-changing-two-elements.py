class Solution:
    # So lets sort the array and consider changing 2 elements.
    # We want to minimize: nums[n] - nums[0] + min(nums[i + 1] - nums[i])
    
    # My thought is to shrink min/max values to the prev values.
    # This would make the second term 0, and minimize the 1st term.
    # 
    def minimizeSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) <= 3:
            return 0
        

        options = [
            nums[-2] - nums[1], # Set min to 2nd smallest, max to 2nd biggest
            nums[-1] - nums[2], # Set 1st/2nd smallest to 3rd smallest
            nums[-3] - nums[0] # Set 1st/2nd largest to 3rd largest
        ]

        return min(options)
        