class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        
        cur = 0
        for ind, count in enumerate(counts):
            for j in range(count):
                nums[cur] = ind
                cur += 1

        