class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numAvail = numBottles
        numEmpty = 0
        numDrank = 0
        while numAvail:
            numDrank += numAvail 
            numEmpty += numAvail
            numAvail = 0

            while numEmpty >= numExchange:
                numAvail += 1
                numEmpty -= numExchange
                numExchange += 1

        return numDrank
        