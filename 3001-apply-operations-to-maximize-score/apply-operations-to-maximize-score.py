from math import floor, ceil

class Solution:
    def solveLastIndForEachPivot(self, primeScores, firstElementIndex):
        curList = []
        resulting_inds = [-1 for i in range(len(primeScores))]
        if firstElementIndex == 0:
            nextElInc = 1
            iterationRange = range(len(primeScores))
        else:
            nextElInc = -1
            iterationRange = range(len(primeScores) - 1, - 1, -1)

        for ind in iterationRange:
            while curList and (
                firstElementIndex == 0 and primeScores[ind] > primeScores[curList[-1]]
                or firstElementIndex > 0 and primeScores[ind] >= primeScores[curList[-1]]
                ):
                # If we are bigger than last element being considered, we can include it in our array and keep this as pivot
                curList.pop()
            
            if not curList:
                maxStartInd = firstElementIndex
            else:
                # We are bigger than all elements until this one
                maxStartInd = curList[-1] + nextElInc 
            
            resulting_inds[ind] = maxStartInd
            curList.append(ind)


        return resulting_inds

    def getPrimeScores(self, nums):
        n = max(nums)
        primeScores = [0 for i in range(n+ 1)]
        for num in range(2, n + 1):
            if primeScores[num] > 0:
                continue
            
            # new prime number
            mult = 1
            while num * mult <= n:
                primeScores[num * mult] += 1
                mult += 1
        
        numScores = []
        for num in nums:
            numScores.append(primeScores[num])
        return numScores
        
    
    def fastPowerWithMod(self, base, power):
        if power == 1:
            return base
        
        if power in self.fastPowerSols:
            return self.fastPowerSols[power]
        
        left = floor(power / 2)
        right = ceil(power / 2)
        result = (self.fastPowerWithMod(base, left) % (10**9 + 7)) * (self.fastPowerWithMod(base, right) % (10**9 + 7))
        answer = result % (10**9 + 7)
        self.fastPowerSols[power] = answer
        return answer

    def maximumScore(self, nums: List[int], k: int) -> int:
        # We want to keep choosing the max elements. You can start at len = 1, and expand left and right to get tot # of arrays
        # We first need to compute the prime scores
        # Then: for each number, we need to know how many arrays can include it as the pivot
            # Solve this in by going in each direction, and just using a stack to track how far we can go
        # Then: take biggest elements in order, and keep including the num arrays
        primeScores = self.getPrimeScores(nums)
        

        ##print(primeScores)
        minIndexPossibleForArrayPivot = self.solveLastIndForEachPivot(primeScores, 0)
        
        ##print(minIndexPossibleForArrayPivot)
        maxIndexPossibleForArrayPivot = self.solveLastIndForEachPivot(primeScores, len(nums) - 1)
        
        ##print(maxIndexPossibleForArrayPivot)

        pivotList = sorted([(nums[i], i) for i in range(len(nums))], reverse = True)
        

        score = 1

        #print(pivotList[:5])
        for value, ind in pivotList:
            numStarts = ind - minIndexPossibleForArrayPivot[ind] + 1
            numEnds = maxIndexPossibleForArrayPivot[ind] - ind + 1
            #print("Value", value, "at", ind, "can start at", minIndexPossibleForArrayPivot[ind], "and end at", maxIndexPossibleForArrayPivot[ind])
            #print("Total possible combos is", numStarts, "*", numEnds)
            numUsed = numStarts * numEnds
            if numUsed >= k:
                numUsed = k

            self.fastPowerSols = {}
            score *= self.fastPowerWithMod(value, numUsed)
            score %= (10**9 +7)
            #print("Score is now", score)
            k -= numUsed
            if k == 0:
                break


        return score % (10**9 +7)