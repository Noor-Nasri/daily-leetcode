class Solution:
    # The medium version is without dupes, and thats just binary search based on [0] vs [mid]
    # The idea is that when we find a value >= nums[0], we are still ascending. So min is later
    # So why cant we just use that again?
    
    # The problem: If [0] is duplicated to [-1], then seeing that value doesnt tell us where to go.
    # But thats not really a big problem. Once we isolate the last val == [0], we can just BS on that.
    
    def findMinIgnoreDupes(self, nums: List[int], high) -> int:
        low = 0
        best = nums[0]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= nums[0]:
                low = mid + 1
            else:
                best = nums[mid]
                high = mid - 1

        return best  

    def findMin(self, nums: List[int]) -> int:
        high = len(nums) - 1
        while high and nums[high] == nums[0]:
            high -= 1
        
        return self.findMinIgnoreDupes(nums, high)

        