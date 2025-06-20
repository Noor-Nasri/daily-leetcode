class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minNum = nums[0]
        maxNum = nums[0]
        # [1] 3     --> 0
        for num in nums:
            if minNum < num < maxNum:
                return num

            if num < minNum:
                if minNum != maxNum:
                    return minNum

                minNum = num
            if num > maxNum:
                if minNum != maxNum:
                    return maxNum

                maxNum = num

        return -1
        