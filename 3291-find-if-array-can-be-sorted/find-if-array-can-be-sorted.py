class Solution:
    def setbit(self, num):
        return sum([int(e) for e in str(bin(num))[2:]])
    def matching(self, num1, num2):
        return self.setbit(num1) == self.setbit(num2)

    def canSortArray(self, nums: List[int]) -> bool:
        # since n <= 100, we can bubble sort with this constraint
        for i in range(len(nums)):
            for ind in range(len(nums) - 1):
                if nums[ind] > nums[ind + 1] and self.matching(nums[ind], nums[ind + 1]):
                    temp = nums[ind]
                    nums[ind] = nums[ind + 1]
                    nums[ind + 1] = temp

        return nums == sorted(nums)    
        