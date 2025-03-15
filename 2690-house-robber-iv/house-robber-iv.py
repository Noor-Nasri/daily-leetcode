class Solution:
    def canStealKHousesWithCapability(self, nums, k, capability):
        ind = 0

        while ind < len(nums) and k:
            if nums[ind] <= capability:
                ind += 1
                k -= 1

            ind += 1

        return k == 0

    def minCapability(self, nums: List[int], k: int) -> int:
        low = 1
        high = max(nums)
        best = high

        while low <= high:
            mid = (low + high)//2
            if self.canStealKHousesWithCapability(nums, k, mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return best
        