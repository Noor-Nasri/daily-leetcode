class Solution:
    def numOperationsGivenInit(self, s, firstChar):
        initValues = [int(e) for e in s]
        diffs = [abs((firstChar + ind) % 2 - initValues[ind]) for ind in range(len(s))]
        return sum(diffs)
        
    def minOperations(self, s: str) -> int:
        return min(self.numOperationsGivenInit(s, 0), self.numOperationsGivenInit(s, 1))
        