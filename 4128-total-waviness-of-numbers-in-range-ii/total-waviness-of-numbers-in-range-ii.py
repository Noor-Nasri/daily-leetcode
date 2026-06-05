class Solution:
    # So we need to derive some math trick here. Instead of going through each number (10^15)
    # Can we select numWaves (< 8) and solve for the number of candidate nums in range?    
    # 1 wave could mean ind1 > ind0,ind2. Maybe simplify math as DP?
    # DP: (digitInd, lastDigitVal, matchingNum1, matchingNum2) -> Iter on (digit, nextDigit): return total waves found

    # This should work .. the trick is that it combines diff number prefixes into the DP mode
    # But since every decision leads to a unique number, we dont have to worry about overlap
    # The other distinction is we dont care how much waviness the specific number has, but all values

    def totalCount(self, digitInd, lastDigitVal, lastDigitMode, matchingMin, matchingMax):
        # Ended up a bit more complicated with choosing two inds at once ..
        # lastDigitMode = 0 equal to previous. 1 = Smaller, 2 = Bigger.
        # Time Limit: InputSpace*InnerComplexity*numScopes 
        # = (15 * 10 * 3 * 2 * 2) * (10 * 10) * (15) = 2,700,000

        uid = (digitInd, lastDigitVal, lastDigitMode, matchingMin, matchingMax)
        if uid in self.sols:
            return self.sols[uid]
        elif digitInd >= self.numDigits:
            return 0, 1  #All inds already chosen, only 1 validDescendants and no more waves

        totalWaves = 0
        validDescendants = 0 
        rangeStart, rangeEnd = 0, 9
        if matchingMin:
            rangeStart = self.digits1[digitInd]
        if matchingMax:
            rangeEnd = self.digits2[digitInd] 

        #print(f"Range1: ", rangeStart, rangeEnd)
        for digit in range(rangeStart, rangeEnd + 1):
            isPrevValley = lastDigitMode == 1 and lastDigitVal < digit
            isPrevPeak = lastDigitMode == 2 and lastDigitVal > digit
            if digitInd == self.numDigits - 1:
                # No next digit: Just count if our choice made the prev a wave
                validDescendants += 1
                totalWaves += int(isPrevValley or isPrevPeak)
                continue

            matchingMin2 = matchingMin and digit == self.digits1[digitInd]
            matchingMax2 = matchingMax and digit == self.digits2[digitInd]
            rangeStart2, rangeEnd2 = 0, 9
            if matchingMin2:
                rangeStart2 = self.digits1[digitInd + 1]
            if matchingMax2:
                rangeEnd2 = self.digits2[digitInd + 1] 

            #print(f"Range2: ", rangeStart2, rangeEnd2)
            for nextDigit in range(rangeStart2, rangeEnd2 + 1):
                if nextDigit > digit:
                    nextDigitMode = 2
                elif nextDigit < digit:
                    nextDigitMode = 1
                else:
                    nextDigitMode = 0

                matchingMin3 = matchingMin2 and nextDigit == self.digits1[digitInd + 1]
                matchingMax3 = matchingMax2 and nextDigit == self.digits2[digitInd + 1]

                wavesWithinDescendants, numDescendants = self.totalCount(digitInd + 2, nextDigit, nextDigitMode, matchingMin3, matchingMax3)
                #print(f"--- Exploring {digit}, {nextDigit}: ")
                #print(f"wavesWithinDescendants={wavesWithinDescendants}, numDescendants={numDescendants}")
                totalWaves += wavesWithinDescendants
                validDescendants += numDescendants

                isPeak = digit > lastDigitVal and digit > nextDigit
                isValley = digit < lastDigitVal and digit < nextDigit

                newWavesFoundInPath = int(isPrevValley or isPrevPeak) + int(isPeak or isValley)
                totalWaves += numDescendants * newWavesFoundInPath

        self.sols[uid] = (totalWaves, validDescendants)
        return self.sols[uid]
        

    def totalWaviness(self, num1: int, num2: int) -> int:
        self.digits1 = [int(e) for e in str(num1)] 
        self.digits2 = [int(e) for e in str(num2)]
        nDigitsMin, nDigitsMax = len(self.digits1), len(self.digits2)

        total = 0
        for numDigits in range(max(3, nDigitsMin), nDigitsMax + 1):
            for digit0 in range(1, 10):
                if numDigits == nDigitsMin and digit0 < self.digits1[0]:
                    continue
                elif numDigits == nDigitsMax and digit0 > self.digits2[0]:
                    continue
                
                #print(f"===== For numDigits={numDigits}, digit0={digit0} =====")
                self.sols = {}
                self.numDigits = numDigits

                matchingMin = numDigits == nDigitsMin and digit0 == self.digits1[0]
                matchingMax = numDigits == nDigitsMax and digit0 == self.digits2[0]
                totalWaves, validDescendants = self.totalCount(1, digit0, 0, matchingMin, matchingMax)

                #print(f"TOTAL: we have totalWaves={totalWaves}, validDescendants={validDescendants}")
                #print(self.sols)
                total += totalWaves

        return total