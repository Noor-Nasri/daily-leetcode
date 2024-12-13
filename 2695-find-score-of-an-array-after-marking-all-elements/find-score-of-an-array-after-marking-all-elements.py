class Solution:
    def findScore(self, nums: List[int]) -> int:
        vals = sorted([(nums[ind], ind) for ind in range(len(nums))])
        marked = [0 for i in range(len(nums))]
        total = 0

        for val, ind in vals:
            if marked[ind]: continue
            total += val
            marked[ind] = 1
            if ind:
                marked[ind - 1] = 1
            if ind < len(nums) - 1:
                marked[ind + 1] = 1
            

        return total
        