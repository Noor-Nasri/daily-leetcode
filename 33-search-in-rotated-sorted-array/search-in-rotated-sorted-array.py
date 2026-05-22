class Solution:
    # Classic binary search question, do it in two phases
    # First we look for the 'drop', ie first val < nums[0] is the real start.
    # Then we check [0], min, [-1] to know which half the value is in, and do regular BS

    def searchForDrop(self, nums):    
        low, high = 0, len(nums) - 1
        best = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[0]:
                best = mid
                high = mid - 1
            else:
                low = mid + 1

        return best
    
    def regularBS(self, nums, target, low, high):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        if nums[0] > nums[-1]:
            realMin = self.searchForDrop(nums)
            if target >= nums[0]:
                high = realMin - 1
            else:
                low = realMin
        
        return self.regularBS(nums, target, low, high)