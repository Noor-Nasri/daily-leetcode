from math import ceil

class Solution:
    def isPenaltyDoable(self, nums, maxOperations, penalty):
        operationsMade = 0

        for value in nums:
            if value <= penalty:
                continue

            excess = value - penalty
            extraBags = ceil(excess / penalty)
            operationsMade += extraBags
            if operationsMade > maxOperations:
                return False

        return True
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # we need to assign a number of final bags per initial bag
        # bags = [(initial, numBags)], sorted by ceil(initial/numBags)
        # Normally: keep increasing numBags for biggest one, until numOperations
        # But numOperations is 10^9. Instead do BS to select penalty, then verify if possible

        low = 1
        high = max(nums)
        bestFound = high

        while low <= high:
            mid = (low + high) // 2
            if self.isPenaltyDoable(nums, maxOperations, mid):
                bestFound = mid
                high = mid - 1
            else:
                low = mid + 1

        return bestFound