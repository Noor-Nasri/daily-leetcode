class Solution:
    # isnt this identical to the one we just solved? n^2 is fine here too
    
    def maxScore(self, rangeStart, rangeEnd):
        uid = (rangeStart, rangeEnd)
        if uid in self.sols:
            return self.sols[uid]
        elif rangeStart > rangeEnd:
            return 0
        
        op1 = self.nums[rangeStart] - self.maxScore(rangeStart + 1, rangeEnd)
        op2 = self.nums[rangeEnd] - self.maxScore(rangeStart, rangeEnd - 1)
        self.sols[uid] = max(op1, op2)
        return self.sols[uid]

    def stoneGame(self, piles: List[int]) -> bool:
        self.sols = {}
        self.nums = piles
        return self.maxScore(0, len(piles) - 1) >= 0
        