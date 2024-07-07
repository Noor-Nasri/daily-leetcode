class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numEmpty = 0
        tot = 0
        while numBottles:
            tot += numBottles
            numEmpty += numBottles
            numBottles = numEmpty // numExchange
            numEmpty -= numBottles * numExchange

        return tot
        