class Solution:
    def canSolve(self, nums, p, maxDiffAllowed):
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= maxDiffAllowed:
                p -= 1
                i += 1
                if p == 0:
                    return True
            i += 1

        return False

    def minimizeMax(self, nums: List[int], p: int) -> int:
        # 1 1 2 3 7 10 -> (1, 1) (1, 2) (2, 3) (7, 10)
        # Question: Would you ever not take lowest pair ?
        # eg: 1 5 7 11 and need two pairs.
        # (5, 7) is smallest pair but then you force 1, 11 together. So should sacrifice for 1, 11
        # How about binary search? Just pick the max dist and see if we can work with it
        if p == 0: 
            return 0

        nums = sorted(nums)
        low = 0
        high = nums[-1] - nums[0]
        best = -1

        while low <= high:
            m = (low + high) // 2
            if self.canSolve( nums, p, m):
                best = m
                high = m - 1
            else:
                low = m + 1

        return best
        