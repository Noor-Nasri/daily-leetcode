class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        counts = [0, 0]
        for num in nums:
            if num == 0:
                continue

            ind = int(num > 0)
            counts[ind] += 1

        return max(counts)
        