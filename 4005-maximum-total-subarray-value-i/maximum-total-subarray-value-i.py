class Solution:
    # It seems like we just find the subarr with maximal value, and choose it k times
    # Why not just.. take the whole array? Just k*(max - min)? What am I missing here?

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))
          