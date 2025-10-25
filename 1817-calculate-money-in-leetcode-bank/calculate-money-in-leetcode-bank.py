class Solution:
    # The pattern is (1 -> 7) + (1 -> 7) (+7) + (1 -> 7) (+2*7) + ..
    # n // 7 tells us the # of full cycles, and we compute 28*c + 7*(0 + 1 + .. + (c - 1))
    # = 28*c + 7 * (c - 1)/2 * c = c * (28 + 3.5c - 3.5) = 3.5c^2 + 24.5c
    def totalMoney(self, n: int) -> int:
        numCycles = n//7
        tot = 3.5*(numCycles**2) + 24.5 * numCycles

        valOfLastMon = numCycles + 1
        numDaysInLastCycle = n % 7

        for remVal in range(valOfLastMon, valOfLastMon + numDaysInLastCycle):
            tot += remVal
        
        return int(tot)

        