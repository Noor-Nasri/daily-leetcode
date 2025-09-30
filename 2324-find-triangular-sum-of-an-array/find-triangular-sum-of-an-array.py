class Solution:
    # Okay, this seems pretty easy because we can just simulate with n^2 and it'll pass
    # There is also a math approach here to make it O(n) because we know how many times the number gets added
    # So we can ignore the %10 till the end. The sum is just pascals triangle, flip the tree upside down
    
    # Maybe more of a headache because the mods can throw off the contribution amounts. Just simulate and move on bruh..
    

    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nextNums = []
            for ind in range(len(nums) - 1):
                nextNums.append(
                    (nums[ind] + nums[ind + 1]) % 10
                )
            
            nums = nextNums
        return nums[0]
        