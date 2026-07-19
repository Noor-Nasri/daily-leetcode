class Solution:
    # My first thought is a greedy or DP. Ideally we'd pick A as first letter, to do this we just need remaining vals to all exist
    # If not, then we need to look for earliest B. and so on.

    # So this means: We select one letter at a time, and each one needs to know its init position (logN BS)
    # and each position needs to know what remaining letters exist afterwards (precomputed in backward sweep)
    # Then we just verify if all remaining letters are still available (check 26)
    # So overall this is actually O(n) precomputation and the rest is (26^3)log(n)
    # First 26 is the overall char loop, next 26 is choosing smallest letter, last 26 is verifying acceptance
    
    def getEarliestIndAfterCutoff(self, allInds, curIndCutoff):
        low = 0
        high = len(allInds) - 1
        best = -1

        while low <= high:
            mid = (low + high) // 2
            if allInds[mid] > curIndCutoff:
                best = allInds[mid]
                high = mid - 1
            else:
                low = mid + 1

        assert(best != -1)
        return best
    
    def verifyViablity(self, availableLetters, requiredLetters):
        for ordVal in requiredLetters:
            if not availableLetters[ordVal]:
                #print("not sufficient - letter", chr(ordVal + ord('a')), "is not available from this ind")
                return False
        
        return True

    def smallestSubsequence(self, s: str) -> str:
        # Basic precompute these tables
        availableLetters = [False for i in range(26)]
        lettersFromInd = [None for i in range(len(s))]
        charInds = [[] for i in range(26)]

        for ind in range(len(s)):
            charInds[ord(s[ind]) - ord('a')].append(ind)

        for ind in range(len(s) -1, -1, -1):
            availableLetters[ord(s[ind]) - ord('a')] = True
            lettersFromInd[ind] = availableLetters[:]
        

        remaining = {i for i in range(26) if availableLetters[i]}
        bestOrder = []
        curIndCutoff = -1

        while remaining:
            #print("---- Loooking for next char ----")
            for nextChar in range(26):
                if nextChar not in remaining:
                    continue
                
                potentialInd = self.getEarliestIndAfterCutoff(charInds[nextChar], curIndCutoff)
                #print("Looking at", chr(nextChar + ord('a')), "which would come from ind", potentialInd)
                if not self.verifyViablity(lettersFromInd[potentialInd], remaining):
                    continue
                
                #print("CHOSEN!")
                bestOrder.append(nextChar)
                remaining.remove(nextChar)
                curIndCutoff = potentialInd
                break

        solution = "".join([chr(e + ord('a')) for e in bestOrder])
        return solution