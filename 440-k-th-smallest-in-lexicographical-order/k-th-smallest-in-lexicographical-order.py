class Solution:
    def getCountOfPrefix(self, value):
        # get count of values with prefix [value] that are <= self.max
        # ie: 12 has [120, 129], [1200, 1299], ...

        count = 0
        power = 1
        while value * (10 ** power) <= self.max:
            numsStart = value * (10 ** power)
            numsEnd = min(numsStart + (10 ** power) - 1, self.max)
            count += numsEnd - numsStart + 1
            power += 1

        return count

    def recurSolve(self, curVal, indexWanted):
        print("Instructed to solve with", curVal, indexWanted)
        if indexWanted == 0: 
            return curVal
        
        if curVal:
            seenSoFar = 1
        else:
            seenSoFar = 0
        
        for nextDigit in range (10):
            if not curVal and not nextDigit: continue # cant start with 0
            nextVal = curVal*10 + nextDigit
            if nextVal > self.max: continue

            count = 1 + self.getCountOfPrefix(nextVal)
            print("Looking at prefix", nextVal, "has", count)
            if indexWanted < seenSoFar + count:
                return self.recurSolve(nextVal, indexWanted - seenSoFar)
            
            seenSoFar += count

        return -1 

    def findKthNumber(self, n: int, k: int) -> int:
        if k == 1: return 1
        self.max = n
        return self.recurSolve(0, k - 1)

        