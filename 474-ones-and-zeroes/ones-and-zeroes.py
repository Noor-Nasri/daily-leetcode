class Solution:
    # Seems like simple DP: At each ind, we include or don't include. Affects limit
    # O(len*m*n) ~ 6,000,000 should be okay

    def solveFromInd(self, ind, remZeros, remOnes):
        uid = (ind, remZeros, remOnes)
        if uid in self.sols:
            return self.sols[uid]
        elif ind == len(self.nOnes):
            return 0
        
        op1 = self.solveFromInd(ind + 1, remZeros, remOnes)
        op2 = 0
        if remOnes >= self.nOnes[ind] and remZeros >= self.nZeros[ind]:
            op2 = 1 + self.solveFromInd(ind + 1, remZeros -  self.nZeros[ind], remOnes - self.nOnes[ind])
        
        self.sols[uid] = max(op1, op2)
        return self.sols[uid]
        
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.nOnes = [e.count('1') for e in strs]
        self.nZeros = [len(strs[i]) - self.nOnes[i] for i in range(len(strs))]
        self.sols = {}
        return self.solveFromInd(0, m, n)