class Solution:
    # DP: (ind1, ind2). When the vals are equal, we can choose to keep the characters instead of delete

    def minCostFromInds(self, ind1, ind2):
        if ind1 == len(self.s1) and ind2 == len(self.s2):
            return 0
        elif ind1 > len(self.s1) or ind2 > len(self.s2):
            return -1
        elif (ind1, ind2) in self.sols:
            return self.sols[(ind1, ind2)]

        bestOption = -1
        if ind1 < len(self.s1) and ind2 < len(self.s2) and self.s1[ind1] == self.s2[ind2]:
            bestOption = self.minCostFromInds(ind1 + 1, ind2 + 1)
        else:
            op1 = self.minCostFromInds(ind1 + 1, ind2)
            op2 = self.minCostFromInds(ind1, ind2 + 1)
            if op1 > -1 and op2 > -1:
                bestOption = min(op1 + ord(self.s1[ind1]), op2 + ord(self.s2[ind2]))
            elif op1 > -1:
                bestOption = op1 + ord(self.s1[ind1])
            elif op2 > -1:
                bestOption = op2 + ord(self.s2[ind2])
                    
        self.sols[(ind1, ind2)] = bestOption
        return bestOption

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.sols = {}
        self.s1 = s1
        self.s2 = s2
        return self.minCostFromInds(0, 0)
