class Solution:
    def maxPointsFromQuestion(self, ind):
        if ind in self.sols:
            return self.sols[ind]
        if ind >= len(self.questions):
            return 0
        

        op1 = self.questions[ind][0] + self.maxPointsFromQuestion(ind + self.questions[ind][1] + 1)
        op2 =  self.maxPointsFromQuestion(ind + 1)
        result = max(op1, op2)
        self.sols[ind] = result
        return self.sols[ind]

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.sols = {}
        self.questions = questions
        return self.maxPointsFromQuestion(0)