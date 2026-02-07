class Solution:
    # We just need to pick the ind of the last a, and remove all a/b out of place
    def minimumDeletions(self, s: str) -> int:
        indToAValue = [e=='a' and 1 or 0 for e in s]
        numAsBeforeInd = [0]
        for v in indToAValue:
            numAsBeforeInd.append(numAsBeforeInd[-1] + v)
        
        minDeletions = len(s)
        for firstBInd in range(len(s) + 1):
            bRemovals = firstBInd - numAsBeforeInd[firstBInd]
            aRemovals = numAsBeforeInd[-1] - numAsBeforeInd[firstBInd]
            minDeletions = min(minDeletions, aRemovals + bRemovals)

        return minDeletions