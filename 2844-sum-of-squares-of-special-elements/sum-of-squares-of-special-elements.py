class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        tot = 0
        n = len(nums)

        for ind in range(len(nums)):
            if not (n % (ind + 1)):
                tot += nums[ind]**2
        
        return tot
        