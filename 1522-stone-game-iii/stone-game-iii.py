class Solution:
    # I dont really get why this is hard, and its like the same as last 2 days. Okay sure then
    # We just do DP(ind) -> maxScore. O(n)
    
    def maxScore(self, rangeStart):
        if rangeStart in self.sols:
            return self.sols[rangeStart]
        elif rangeStart >= len(self.vals):
            return 0
        
        options = []
        curBonus = 0
        for optionalInd in range(rangeStart, min(rangeStart + 3, len(self.vals))):
            curBonus += self.vals[optionalInd]
            options.append(curBonus - self.maxScore(optionalInd + 1))

        self.sols[rangeStart] = max(options)
        return self.sols[rangeStart]

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.vals = stoneValue
        self.sols = {}
        finalDiff = self.maxScore(0)

        if finalDiff > 0:
            return "Alice"
        elif finalDiff < 0:
            return "Bob"
        
        return "Tie"
        
        