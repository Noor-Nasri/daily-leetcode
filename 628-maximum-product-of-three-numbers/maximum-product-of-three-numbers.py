class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)

        if nums[0]*nums[1] > nums[-2]*nums[-3] and nums[-1] > 0: 
            # Replace 2nd and 3rd best with two negatives
            return nums[0]*nums[1]*nums[-1]
        return nums[-1]*nums[-2]*nums[-3]