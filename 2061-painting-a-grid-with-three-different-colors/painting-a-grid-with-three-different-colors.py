class Solution:
    def setAllPossibleColumns(self):
        curOptions = [ [] ]
        for i in range(self.m):
            newOptions = []
            for option in curOptions:
                for nextCol in range(3):
                    if option and nextCol == option[-1]: continue
                    newOption = option + [nextCol]
                    newOptions.append(newOption)
            curOptions = newOptions
        
        self.allValidCols = [tuple(e) for e in curOptions]

    def isValidNextCol(self, prevCol, col):
        for ind_row in range(len(prevCol)):
            if col[ind_row] == prevCol[ind_row]:
                return False
        
        return True

    def numCombos(self, ind, prevCol):
        if ind == self.n:
            return 1

        if (ind, prevCol) in self.sols:
            return self.sols[(ind, prevCol)]
        

        numWays = 0
        for col in self.allValidCols:
            if self.isValidNextCol(prevCol, col):
                numWays += self.numCombos(ind + 1, col)
                numWays %= (10**9 + 7)

        self.sols[(ind, prevCol)] = numWays
        return numWays

    def colorTheGrid(self, m: int, n: int) -> int:
        self.sols = {}
        self.m = m
        self.n = n

        self.setAllPossibleColumns()
        return self.numCombos(0, tuple([-1 for i in range(m)]))