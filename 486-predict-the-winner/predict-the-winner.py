class Solution:
    # There is a game theory solve here but also n is so small, can do 2^n
    # DP would be: (range1, range2, playerTurn): -> returns max score for current player
    # That would just be n^2, no problem at all here

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

    def predictTheWinner(self, nums: List[int]) -> bool:
        self.sols = {}
        self.nums = nums
        return self.maxScore(0, len(nums) - 1) >= 0