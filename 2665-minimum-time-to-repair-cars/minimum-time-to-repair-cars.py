from math import floor
class Solution:
    def canCarsBeRepaired(self, ranks, cars, time):
        # r * n^2 = t <--> n = (t/r)**0.5
        print("Investigating", time)
        for rank in ranks:
            numCars = floor((time / rank)**0.5)
            cars -= numCars

            if cars <= 0:
                return True
        return False

    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 0
        high = 100 * cars**2
        best = -1
        while low <= high:
            mid = (low + high) // 2
            if self.canCarsBeRepaired(ranks, cars, mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return best