class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums): return []
        ranges = []
        short = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1: 
                if (i - 1 == short):
                    ranges.append(str(nums[short]))
                else:
                    ranges.append(f"{nums[short]}->{nums[i-1]}")
                short = i

        if short == len(nums) - 1:
            ranges.append(str(nums[-1]))
        else:
            ranges.append(f"{nums[short]}->{nums[-1]}")

        return ranges
        