class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # I misread this question and made it complicated. It's just a basic windownums = sorted(nums)
        nums = sorted(nums)
        startNum = nums[0]
        numSeq = 1
        for num in nums:
            if num - startNum > k:
                startNum = num
                numSeq += 1

        return numSeq
        