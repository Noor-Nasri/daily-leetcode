class Solution:
    # This seems like standard DP: what am I missing?
    # Given (wordInd, finger1Pos, finger2Pos): return min cost
    # Each wordInd gives you two options: finger1 or finger2
    # So thats 300*26*26 input space. Thats totally fine.


    def travelCost(self, fingerPos, letterPos):
        if fingerPos[0] == fingerPos[1] == -1:
            return 0
        
        return abs(letterPos[0] - fingerPos[0]) + abs(letterPos[1] - fingerPos[1])
        
    def costForRemainingWord(self, wordInd, finger1Pos, finger2Pos):
        uid = (wordInd, finger1Pos, finger2Pos)
        if uid in self.sols:
            return self.sols[uid]
        elif wordInd == len(self.word):
            return 0
        
        letterPos = (self.word[wordInd] // 6, self.word[wordInd] % 6)
        cost1 = self.travelCost(finger1Pos, letterPos) + self.costForRemainingWord(wordInd + 1, letterPos, finger2Pos)
        cost2 = self.travelCost(finger2Pos, letterPos) + self.costForRemainingWord(wordInd + 1, finger1Pos, letterPos)
        self.sols[uid] = min(cost1, cost2)
        return self.sols[uid] 

    def minimumDistance(self, word: str) -> int:
        self.sols = {}
        self.word = [ord(e) - ord('A') for e in word]
        return self.costForRemainingWord(0, (-1, -1), (-1, -1))
        