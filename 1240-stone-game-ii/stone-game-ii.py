class Solution:
    def getOptimalMove(self, indStart, M):
        # 100 * 100 possible calls, we don't actually care about player
        if (indStart, M) in self.sols:
            return self.sols[(indStart, M)]
        
        if (indStart >= len(self.piles)):
            return [0, 0]
        
        bestForUs = [0, 0]
        collectRightAway = 0
        for indBonus in range(M*2):
            if indStart + indBonus >= len(self.piles):
                break
            
            collectRightAway += self.piles[indStart + indBonus]
            otherScore, ourScore = self.getOptimalMove(indStart + indBonus + 1, max(indBonus + 1, M))
            if collectRightAway + ourScore > bestForUs[0]:
                bestForUs = [collectRightAway + ourScore, otherScore]

        self.sols[(indStart, M)] = bestForUs
        return bestForUs

    def stoneGameII(self, piles: List[int]) -> int:
        self.sols = {}
        self.piles = piles
        return self.getOptimalMove(0, 1)[0]
        