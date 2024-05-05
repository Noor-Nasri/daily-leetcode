class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numElements = 0
        lastNum = None
        for val in nums:
            if val != lastNum: 
                nums[numElements] = val
                numElements += 1
                lastNum = val

        return numElements
        